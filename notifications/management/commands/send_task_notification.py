"""
Management command to send task completion notifications to Live Great Foundation team
"""

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import json

from notifications.services import email_service


class Command(BaseCommand):
    help = 'Send task completion notification to Live Great Foundation team'

    def add_arguments(self, parser):
        parser.add_argument(
            'title',
            type=str,
            help='Title of the completed task'
        )
        
        parser.add_argument(
            'description',
            type=str,
            help='Description of the completed task'
        )
        
        parser.add_argument(
            '--features',
            type=str,
            help='Comma-separated list of key features delivered'
        )
        
        parser.add_argument(
            '--technical-details',
            type=str,
            help='JSON string of technical implementation details'
        )
        
        parser.add_argument(
            '--next-steps',
            type=str,
            help='Recommended next steps or actions'
        )
        
        parser.add_argument(
            '--type',
            type=str,
            choices=['task_completion', 'system_update', 'feature_release', 'maintenance', 'security_update'],
            default='task_completion',
            help='Type of notification (default: task_completion)'
        )
        
        parser.add_argument(
            '--auto-send',
            action='store_true',
            help='Send email automatically without confirmation prompt'
        )
        
        parser.add_argument(
            '--preview-only',
            action='store_true',
            help='Only show preview without creating or sending notification'
        )

    def handle(self, *args, **options):
        title = options['title']
        description = options['description']
        
        # Parse features
        features_delivered = []
        if options['features']:
            features_delivered = [f.strip() for f in options['features'].split(',') if f.strip()]
        
        # Parse technical details
        technical_details = {}
        if options['technical_details']:
            try:
                technical_details = json.loads(options['technical_details'])
            except json.JSONDecodeError:
                raise CommandError('Invalid JSON format for technical details')
        
        next_steps = options.get('next_steps', '')
        notification_type = options.get('type', 'task_completion')
        auto_send = options.get('auto_send', False)
        preview_only = options.get('preview_only', False)
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🚀 Live Great Foundation - Task Completion Notification'))
        self.stdout.write('=' * 70)
        
        # Show task summary
        self.stdout.write(f'📋 Task: {title}')
        self.stdout.write(f'📝 Description: {description}')
        self.stdout.write(f'🏷️  Type: {notification_type.replace("_", " ").title()}')
        
        if features_delivered:
            self.stdout.write(f'✅ Features ({len(features_delivered)}):')
            for i, feature in enumerate(features_delivered, 1):
                self.stdout.write(f'   {i}. {feature}')
        
        if technical_details:
            self.stdout.write(f'🔧 Technical Details ({len(technical_details)} items):')
            for key, value in technical_details.items():
                self.stdout.write(f'   • {key.title()}: {value}')
        
        if next_steps:
            self.stdout.write(f'📋 Next Steps: {next_steps}')
        
        self.stdout.write('')
        
        # Preview only mode
        if preview_only:
            self.stdout.write(self.style.WARNING('📧 Email Preview Mode - No notification will be created or sent'))
            self.stdout.write('')
            return
        
        # Create notification
        try:
            notification = email_service.create_task_completion_notification(
                title=title,
                description=description,
                features_delivered=features_delivered,
                technical_details=technical_details,
                next_steps=next_steps,
                notification_type=notification_type
            )
            
            self.stdout.write(self.style.SUCCESS(f'✅ Notification created (ID: {notification.id})'))
            
            # Show email preview
            self.stdout.write('')
            self.stdout.write('📧 Email Preview:')
            self.stdout.write('-' * 50)
            preview = email_service.get_notification_preview(notification)
            self.stdout.write(preview)
            self.stdout.write('-' * 50)
            
        except Exception as e:
            raise CommandError(f'Failed to create notification: {str(e)}')
        
        # Send email
        if auto_send:
            self.stdout.write('')
            self.stdout.write('📤 Sending email automatically...')
            sent = email_service.send_notification(notification)
            
            if sent:
                self.stdout.write(self.style.SUCCESS('✅ Email sent successfully!'))
                self.stdout.write(f'📧 Sent to: {notification.recipient_email}')
                self.stdout.write(f'⏰ Sent at: {notification.sent_at.strftime("%Y-%m-%d %H:%M:%S")}')
            else:
                self.stdout.write(self.style.ERROR('❌ Failed to send email'))
                if notification.error_message:
                    self.stdout.write(f'Error: {notification.error_message}')
        else:
            # Interactive confirmation
            self.stdout.write('')
            self.stdout.write(self.style.WARNING('📧 Email Confirmation Required'))
            
            while True:
                response = input('Would you like to send this email notification to the Live Great Foundation team? (y/n): ').lower().strip()
                
                if response in ['y', 'yes']:
                    self.stdout.write('📤 Sending email...')
                    sent = email_service.send_notification(notification)
                    
                    if sent:
                        self.stdout.write(self.style.SUCCESS('✅ Email sent successfully!'))
                        self.stdout.write(f'📧 Sent to: {notification.recipient_email}')
                        self.stdout.write(f'⏰ Sent at: {notification.sent_at.strftime("%Y-%m-%d %H:%M:%S")}')
                    else:
                        self.stdout.write(self.style.ERROR('❌ Failed to send email'))
                        if notification.error_message:
                            self.stdout.write(f'Error: {notification.error_message}')
                    break
                    
                elif response in ['n', 'no']:
                    notification.status = 'cancelled'
                    notification.save()
                    self.stdout.write(self.style.WARNING('🚫 Email sending cancelled'))
                    self.stdout.write('💾 Notification saved for future reference')
                    break
                    
                else:
                    self.stdout.write('Please enter "y" for yes or "n" for no.')
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🎉 Task notification process completed!'))
        self.stdout.write('')


# Example usage:
"""
# Basic usage
python manage.py send_task_notification "Excel Import System" "Created comprehensive Excel template system for AI-assisted blog import"

# With features
python manage.py send_task_notification "Excel Import System" "Created comprehensive Excel template system" --features "Excel template with validation,AI content integration,Bulk import functionality,Admin interface enhancements"

# With technical details
python manage.py send_task_notification "Database Migration" "Migrated from Neon to Supabase" --technical-details '{"database": "Supabase PostgreSQL", "django_version": "5.0.9", "performance": "Optimized connection pooling"}'

# Auto-send without confirmation
python manage.py send_task_notification "Security Update" "Applied security patches" --auto-send

# Preview only
python manage.py send_task_notification "Test Task" "Test description" --preview-only
"""
