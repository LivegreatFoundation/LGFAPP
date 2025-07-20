"""
Email notification services for Live Great Foundation
"""

import logging
from datetime import datetime
from typing import List, Dict, Optional

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

from .models import EmailNotification

logger = logging.getLogger(__name__)


class EmailNotificationService:
    """Service class for handling email notifications"""
    
    def __init__(self):
        self.from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@livegreatfoundation.org')
        self.admin_email = getattr(settings, 'LGF_ADMIN_EMAIL', 'info@livegreatfoundation.org')
        self.enabled = getattr(settings, 'LGF_NOTIFICATION_ENABLED', True)
    
    def create_task_completion_notification(
        self,
        title: str,
        description: str,
        features_delivered: List[str] = None,
        technical_details: Dict = None,
        next_steps: str = "",
        notification_type: str = "task_completion"
    ) -> EmailNotification:
        """
        Create a new task completion notification
        
        Args:
            title: Task title
            description: Task description
            features_delivered: List of key features delivered
            technical_details: Dictionary of technical implementation details
            next_steps: Recommended next steps
            notification_type: Type of notification
            
        Returns:
            EmailNotification instance
        """
        
        # Generate subject line
        date_str = timezone.now().strftime("%B %d, %Y")
        subject = f"Website Update Complete: {title} - {date_str}"
        
        # Create notification record
        notification = EmailNotification.objects.create(
            title=title,
            description=description,
            notification_type=notification_type,
            recipient_email=self.admin_email,
            subject=subject,
            features_delivered=features_delivered or [],
            technical_details=technical_details or {},
            next_steps=next_steps,
            status='pending'
        )
        
        # Generate email content
        notification.email_content = self._generate_email_content(notification)
        notification.save()
        
        logger.info(f"Created notification: {notification.title} (ID: {notification.id})")
        return notification
    
    def send_notification(self, notification: EmailNotification) -> bool:
        """
        Send an email notification
        
        Args:
            notification: EmailNotification instance to send
            
        Returns:
            bool: True if sent successfully, False otherwise
        """
        
        if not self.enabled:
            logger.warning("Email notifications are disabled")
            notification.mark_as_failed("Email notifications are disabled in settings")
            return False
        
        try:
            # Create email message
            email = EmailMultiAlternatives(
                subject=notification.subject,
                body=self._generate_plain_text_content(notification),
                from_email=self.from_email,
                to=[notification.recipient_email]
            )

            # Attach HTML content
            email.attach_alternative(notification.email_content, "text/html")

            # Configure connection with SSL handling
            from django.core.mail import get_connection
            import ssl

            # Create SSL context that's more permissive for Gmail
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            # Send email with custom connection
            connection = get_connection(
                backend='django.core.mail.backends.smtp.EmailBackend',
                host=getattr(settings, 'EMAIL_HOST', 'smtp.gmail.com'),
                port=getattr(settings, 'EMAIL_PORT', 587),
                username=getattr(settings, 'EMAIL_HOST_USER', ''),
                password=getattr(settings, 'EMAIL_HOST_PASSWORD', ''),
                use_tls=True,
                fail_silently=False,
            )

            email.connection = connection
            email.send()

            # Mark as sent
            notification.mark_as_sent()

            logger.info(f"Successfully sent notification: {notification.title} to {notification.recipient_email}")
            return True
            
        except Exception as e:
            error_message = f"Failed to send email: {str(e)}"
            logger.error(f"Email sending failed for notification {notification.id}: {error_message}")
            notification.mark_as_failed(error_message)
            return False
    
    def _generate_email_content(self, notification: EmailNotification) -> str:
        """Generate HTML email content from template"""
        
        template_map = {
            'task_completion': 'notifications/emails/task_completion.html',
            'system_update': 'notifications/emails/task_completion.html',
            'feature_release': 'notifications/emails/task_completion.html',
            'maintenance': 'notifications/emails/task_completion.html',
            'security_update': 'notifications/emails/task_completion.html',
        }
        
        template_name = template_map.get(notification.notification_type, 'notifications/emails/task_completion.html')
        
        context = {
            'notification': notification,
            'current_date': timezone.now(),
            'site_url': getattr(settings, 'SITE_URL', 'http://localhost:8000'),
        }
        
        return render_to_string(template_name, context)
    
    def _generate_plain_text_content(self, notification: EmailNotification) -> str:
        """Generate plain text email content as fallback"""
        
        content = f"""
Live Great Foundation - Website Update Complete

Task: {notification.title}

Description:
{notification.description}

"""
        
        if notification.features_delivered:
            content += "Key Features Delivered:\n"
            for feature in notification.features_delivered:
                content += f"• {feature}\n"
            content += "\n"
        
        if notification.technical_details:
            content += "Technical Details:\n"
            for key, value in notification.technical_details.items():
                content += f"• {key.title()}: {value}\n"
            content += "\n"
        
        if notification.next_steps:
            content += f"Next Steps:\n{notification.next_steps}\n\n"
        
        content += f"""
Completion Date: {notification.created_at.strftime('%B %d, %Y at %I:%M %p')}
Update Type: {notification.get_notification_type_display()}

---
Live Great Foundation Technical Team
Email: info@livegreatfoundation.org
Website: www.livegreatfoundation.org
"""
        
        return content.strip()
    
    def send_task_completion_email(
        self,
        title: str,
        description: str,
        features_delivered: List[str] = None,
        technical_details: Dict = None,
        next_steps: str = "",
        auto_send: bool = False
    ) -> tuple[EmailNotification, bool]:
        """
        Create and optionally send a task completion email
        
        Args:
            title: Task title
            description: Task description  
            features_delivered: List of key features delivered
            technical_details: Dictionary of technical details
            next_steps: Recommended next steps
            auto_send: Whether to send immediately without confirmation
            
        Returns:
            tuple: (EmailNotification instance, bool indicating if sent)
        """
        
        # Create notification
        notification = self.create_task_completion_notification(
            title=title,
            description=description,
            features_delivered=features_delivered,
            technical_details=technical_details,
            next_steps=next_steps
        )
        
        # Send if auto_send is True
        sent = False
        if auto_send:
            sent = self.send_notification(notification)
        
        return notification, sent
    
    def get_notification_preview(self, notification: EmailNotification) -> str:
        """Get a preview of the notification content"""
        
        preview = f"""
Subject: {notification.subject}
To: {notification.recipient_email}
From: {self.from_email}

Task: {notification.title}
Description: {notification.description[:200]}{'...' if len(notification.description) > 200 else ''}

Features: {len(notification.features_delivered)} items
Technical Details: {len(notification.technical_details)} items
Next Steps: {'Yes' if notification.next_steps else 'None'}
"""
        return preview.strip()


# Global service instance
email_service = EmailNotificationService()
