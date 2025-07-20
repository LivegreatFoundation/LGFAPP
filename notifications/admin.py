from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin

from .models import EmailNotification
from .services import email_service


@admin.register(EmailNotification)
class EmailNotificationAdmin(ModelAdmin):
    list_display = [
        'title',
        'notification_type',
        'status_with_icon',
        'recipient_email',
        'created_at',
        'sent_at',
        'action_buttons'
    ]

    list_filter = [
        'status',
        'notification_type',
        'created_at',
        'sent_at'
    ]

    search_fields = [
        'title',
        'description',
        'recipient_email',
        'subject'
    ]

    readonly_fields = [
        'created_at',
        'sent_at',
        'email_content_preview',
        'features_delivered_display',
        'technical_details_display'
    ]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'notification_type')
        }),
        ('Email Details', {
            'fields': ('recipient_email', 'subject', 'status')
        }),
        ('Content', {
            'fields': ('features_delivered_display', 'technical_details_display', 'next_steps'),
            'classes': ('collapse',)
        }),
        ('Email Preview', {
            'fields': ('email_content_preview',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'sent_at'),
            'classes': ('collapse',)
        }),
        ('Error Information', {
            'fields': ('error_message',),
            'classes': ('collapse',)
        }),
    )

    actions = ['send_selected_notifications', 'mark_as_cancelled']

    def status_with_icon(self, obj):
        """Display status with appropriate icon"""
        return obj.get_status_display_with_icon()
    status_with_icon.short_description = 'Status'

    def action_buttons(self, obj):
        """Display action buttons for each notification"""
        buttons = []

        if obj.status == 'pending':
            send_url = reverse('admin:notifications_emailnotification_send', args=[obj.pk])
            buttons.append(
                f'<a href="{send_url}" class="button" style="background-color: #28a745; color: white; padding: 4px 8px; text-decoration: none; border-radius: 3px; font-size: 11px;">📤 Send</a>'
            )

        preview_url = reverse('admin:notifications_emailnotification_preview', args=[obj.pk])
        buttons.append(
            f'<a href="{preview_url}" class="button" style="background-color: #17a2b8; color: white; padding: 4px 8px; text-decoration: none; border-radius: 3px; font-size: 11px;">👁️ Preview</a>'
        )

        return format_html(' '.join(buttons))
    action_buttons.short_description = 'Actions'
    action_buttons.allow_tags = True

    def email_content_preview(self, obj):
        """Display email content preview"""
        if obj.email_content:
            # Show first 500 characters of HTML content
            preview = obj.email_content[:500]
            if len(obj.email_content) > 500:
                preview += "..."

            return format_html(
                '<div style="max-height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; background-color: #f9f9f9;">'
                '<pre style="white-space: pre-wrap; font-size: 12px;">{}</pre>'
                '</div>',
                preview
            )
        return "No content generated"
    email_content_preview.short_description = 'Email Content Preview'

    def features_delivered_display(self, obj):
        """Display features delivered as formatted list"""
        if obj.features_delivered:
            features_html = '<ul style="margin: 0; padding-left: 20px;">'
            for feature in obj.features_delivered:
                features_html += f'<li>{feature}</li>'
            features_html += '</ul>'
            return mark_safe(features_html)
        return "No features specified"
    features_delivered_display.short_description = 'Features Delivered'

    def technical_details_display(self, obj):
        """Display technical details as formatted list"""
        if obj.technical_details:
            details_html = '<dl style="margin: 0;">'
            for key, value in obj.technical_details.items():
                details_html += f'<dt style="font-weight: bold; margin-top: 8px;">{key.title()}:</dt>'
                details_html += f'<dd style="margin-left: 20px; margin-bottom: 4px;">{value}</dd>'
            details_html += '</dl>'
            return mark_safe(details_html)
        return "No technical details specified"
    technical_details_display.short_description = 'Technical Details'

    def send_selected_notifications(self, request, queryset):
        """Admin action to send selected notifications"""
        sent_count = 0
        failed_count = 0

        for notification in queryset.filter(status='pending'):
            if email_service.send_notification(notification):
                sent_count += 1
            else:
                failed_count += 1

        if sent_count > 0:
            self.message_user(request, f'Successfully sent {sent_count} notification(s).')
        if failed_count > 0:
            self.message_user(request, f'Failed to send {failed_count} notification(s).', level='ERROR')

    send_selected_notifications.short_description = "Send selected notifications"

    def mark_as_cancelled(self, request, queryset):
        """Admin action to mark notifications as cancelled"""
        updated = queryset.filter(status='pending').update(status='cancelled')
        self.message_user(request, f'Marked {updated} notification(s) as cancelled.')

    mark_as_cancelled.short_description = "Mark as cancelled"

    def get_urls(self):
        """Add custom URLs for send and preview actions"""
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/send/', self.send_notification_view, name='notifications_emailnotification_send'),
            path('<int:object_id>/preview/', self.preview_notification_view, name='notifications_emailnotification_preview'),
        ]
        return custom_urls + urls

    def send_notification_view(self, request, object_id):
        """Custom view to send a single notification"""
        from django.shortcuts import get_object_or_404, redirect
        from django.contrib import messages

        notification = get_object_or_404(EmailNotification, pk=object_id)

        if notification.status != 'pending':
            messages.error(request, f'Cannot send notification with status: {notification.get_status_display()}')
        else:
            if email_service.send_notification(notification):
                messages.success(request, f'Successfully sent notification: {notification.title}')
            else:
                messages.error(request, f'Failed to send notification: {notification.error_message}')

        return redirect('admin:notifications_emailnotification_changelist')

    def preview_notification_view(self, request, object_id):
        """Custom view to preview notification content"""
        from django.shortcuts import get_object_or_404
        from django.http import HttpResponse

        notification = get_object_or_404(EmailNotification, pk=object_id)

        if notification.email_content:
            return HttpResponse(notification.email_content, content_type='text/html')
        else:
            return HttpResponse('<h1>No email content available</h1><p>Email content has not been generated for this notification.</p>')

    def has_delete_permission(self, request, obj=None):
        """Only allow deletion of failed or cancelled notifications"""
        if obj and obj.status in ['sent']:
            return False
        return super().has_delete_permission(request, obj)
