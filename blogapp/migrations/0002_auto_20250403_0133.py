from django.db import migrations, models
import django.db.models.deletion

def forward_func(apps, schema_editor):
    # Get the historical models
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('blogapp', 'Post')
    
    # Create default admin if doesn't exist
    default_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'is_staff': True,
            'is_superuser': True,
            'email': 'admin@livegreatfoundation.org'
        }
    )
    
    # Update all NULL users to default user
    Post.objects.filter(user__isnull=True).update(user=default_user)

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('blogapp', '0001_initial'),  # Replace with your last migration name
    ]

    operations = [
        # First, run the Python code to set default user
        migrations.RunPython(forward_func, reverse_func),
        
        # Then, alter the field to be non-nullable
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.SET_NULL,
                to='auth.user',
                null=True,  # Keep as True
                related_name='blog_posts'
            ),
        ),
    ]