"""
Utility functions for easy task completion notifications
"""

import sys
from typing import List, Dict, Optional

from .services import email_service


def notify_task_completion(
    title: str,
    description: str,
    features_delivered: List[str] = None,
    technical_details: Dict = None,
    next_steps: str = "",
    notification_type: str = "task_completion",
    auto_confirm: bool = False
) -> bool:
    """
    Easy-to-use function for sending task completion notifications
    
    Args:
        title: Task title
        description: Task description
        features_delivered: List of key features delivered
        technical_details: Dictionary of technical details
        next_steps: Recommended next steps
        notification_type: Type of notification
        auto_confirm: If True, sends without user confirmation
        
    Returns:
        bool: True if email was sent, False otherwise
    """
    
    print("\n" + "="*70)
    print("🚀 Live Great Foundation - Task Completion Notification")
    print("="*70)
    
    # Display task summary
    print(f"📋 Task: {title}")
    print(f"📝 Description: {description}")
    print(f"🏷️  Type: {notification_type.replace('_', ' ').title()}")
    
    if features_delivered:
        print(f"\n✅ Key Features Delivered ({len(features_delivered)}):")
        for i, feature in enumerate(features_delivered, 1):
            print(f"   {i}. {feature}")
    
    if technical_details:
        print(f"\n🔧 Technical Details ({len(technical_details)} items):")
        for key, value in technical_details.items():
            print(f"   • {key.title()}: {value}")
    
    if next_steps:
        print(f"\n📋 Next Steps:")
        print(f"   {next_steps}")
    
    print("\n" + "-"*70)
    
    try:
        # Create notification
        notification = email_service.create_task_completion_notification(
            title=title,
            description=description,
            features_delivered=features_delivered,
            technical_details=technical_details,
            next_steps=next_steps,
            notification_type=notification_type
        )
        
        print(f"✅ Notification created (ID: {notification.id})")
        
        # Show email preview
        print(f"\n📧 Email Preview:")
        print(f"   To: {notification.recipient_email}")
        print(f"   Subject: {notification.subject}")
        print(f"   Content: {len(notification.email_content)} characters")
        
        # Get user confirmation unless auto_confirm is True
        if auto_confirm:
            print("\n📤 Auto-sending email...")
            send_email = True
        else:
            print(f"\n📧 Email Confirmation Required")
            while True:
                try:
                    response = input("Would you like to send this email notification to the Live Great Foundation team? (y/n): ").lower().strip()
                    
                    if response in ['y', 'yes']:
                        send_email = True
                        break
                    elif response in ['n', 'no']:
                        send_email = False
                        break
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                except KeyboardInterrupt:
                    print("\n🚫 Operation cancelled by user")
                    notification.status = 'cancelled'
                    notification.save()
                    return False
        
        # Send email if confirmed
        if send_email:
            print("📤 Sending email...")
            sent = email_service.send_notification(notification)
            
            if sent:
                print("✅ Email sent successfully!")
                print(f"📧 Sent to: {notification.recipient_email}")
                print(f"⏰ Sent at: {notification.sent_at.strftime('%Y-%m-%d %H:%M:%S')}")
                print("\n🎉 Task notification completed successfully!")
                return True
            else:
                print("❌ Failed to send email")
                if notification.error_message:
                    print(f"Error: {notification.error_message}")
                return False
        else:
            notification.status = 'cancelled'
            notification.save()
            print("🚫 Email sending cancelled")
            print("💾 Notification saved for future reference")
            return False
            
    except Exception as e:
        print(f"❌ Error creating notification: {str(e)}")
        return False
    
    finally:
        print("="*70 + "\n")


def quick_task_notification(title: str, description: str, features: str = "") -> bool:
    """
    Quick and simple task notification with minimal parameters
    
    Args:
        title: Task title
        description: Task description  
        features: Comma-separated string of features
        
    Returns:
        bool: True if email was sent, False otherwise
    """
    
    features_list = []
    if features:
        features_list = [f.strip() for f in features.split(',') if f.strip()]
    
    return notify_task_completion(
        title=title,
        description=description,
        features_delivered=features_list
    )


def notify_system_update(
    title: str,
    description: str,
    components_updated: List[str] = None,
    version_info: Dict = None,
    breaking_changes: str = ""
) -> bool:
    """
    Specialized function for system update notifications
    
    Args:
        title: Update title
        description: Update description
        components_updated: List of system components updated
        version_info: Dictionary with version information
        breaking_changes: Description of any breaking changes
        
    Returns:
        bool: True if email was sent, False otherwise
    """
    
    technical_details = version_info or {}
    next_steps = breaking_changes if breaking_changes else ""
    
    return notify_task_completion(
        title=title,
        description=description,
        features_delivered=components_updated,
        technical_details=technical_details,
        next_steps=next_steps,
        notification_type="system_update"
    )


def notify_feature_release(
    title: str,
    description: str,
    new_features: List[str] = None,
    improvements: List[str] = None,
    user_impact: str = ""
) -> bool:
    """
    Specialized function for feature release notifications
    
    Args:
        title: Feature release title
        description: Release description
        new_features: List of new features
        improvements: List of improvements
        user_impact: Description of user impact
        
    Returns:
        bool: True if email was sent, False otherwise
    """
    
    all_features = []
    if new_features:
        all_features.extend([f"NEW: {feature}" for feature in new_features])
    if improvements:
        all_features.extend([f"IMPROVED: {improvement}" for improvement in improvements])
    
    return notify_task_completion(
        title=title,
        description=description,
        features_delivered=all_features,
        next_steps=user_impact,
        notification_type="feature_release"
    )


# Example usage functions for testing
def example_usage():
    """Example usage of the notification functions"""
    
    print("Example 1: Basic task notification")
    notify_task_completion(
        title="Excel Import System Implementation",
        description="Created comprehensive Excel template system for AI-assisted bulk blog post creation and import.",
        features_delivered=[
            "Excel template with data validation",
            "AI content integration prompts",
            "Bulk import functionality",
            "Admin interface enhancements",
            "Mobile-responsive design"
        ],
        technical_details={
            "Django Version": "5.0.9",
            "Database": "Supabase PostgreSQL", 
            "Admin Theme": "django-unfold",
            "Import Library": "django-import-export"
        },
        next_steps="Train content team on the new workflow and begin AI-assisted content creation."
    )
    
    print("\nExample 2: Quick notification")
    quick_task_notification(
        title="Database Migration Complete",
        description="Successfully migrated from Neon to Supabase database",
        features="Improved performance, Better reliability, Enhanced security"
    )
    
    print("\nExample 3: System update")
    notify_system_update(
        title="Django 5.0 Upgrade",
        description="Upgraded Django framework from 3.2 to 5.0",
        components_updated=["Django Core", "Admin Interface", "Database Layer"],
        version_info={"Previous": "3.2.20", "Current": "5.0.9", "Python": "3.12"},
        breaking_changes="Updated admin templates may require review"
    )


if __name__ == "__main__":
    # Run examples if script is executed directly
    example_usage()
