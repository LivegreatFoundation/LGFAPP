from django.db import models
from django.utils import timezone


class EmailNotification(models.Model):
    """Model to track email notifications sent to the LGF team"""

    NOTIFICATION_TYPES = [
        ('task_completion', 'Task Completion'),
        ('system_update', 'System Update'),
        ('feature_release', 'Feature Release'),
        ('maintenance', 'Maintenance'),
        ('security_update', 'Security Update'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    # Basic Information
    title = models.CharField(max_length=200, help_text="Task or update title")
    description = models.TextField(help_text="Detailed description of the task/update")
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default='task_completion'
    )

    # Email Details
    recipient_email = models.EmailField(default='info@livegreatfoundation.org')
    subject = models.CharField(max_length=300)
    email_content = models.TextField(help_text="HTML email content")

    # Status and Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, help_text="Error details if sending failed")

    # Metadata
    features_delivered = models.JSONField(
        default=list,
        help_text="List of key features or improvements delivered"
    )
    technical_details = models.JSONField(
        default=dict,
        help_text="Technical implementation details"
    )
    next_steps = models.TextField(blank=True, help_text="Recommended next steps or actions")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Email Notification"
        verbose_name_plural = "Email Notifications"

    def __str__(self):
        return f"{self.title} - {self.status} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

    def mark_as_sent(self):
        """Mark notification as successfully sent"""
        self.status = 'sent'
        self.sent_at = timezone.now()
        self.save()

    def mark_as_failed(self, error_message):
        """Mark notification as failed with error details"""
        self.status = 'failed'
        self.error_message = error_message
        self.save()

    def get_status_display_with_icon(self):
        """Get status with appropriate emoji icon"""
        status_icons = {
            'pending': '⏳',
            'sent': '✅',
            'failed': '❌',
            'cancelled': '🚫',
        }
        return f"{status_icons.get(self.status, '❓')} {self.get_status_display()}"
