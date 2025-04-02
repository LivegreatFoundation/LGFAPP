# Generated by Django 3.2.20 on 2025-03-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_secondsection_secondsectionbox_secondsectionicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editpage',
            name='section_name',
            field=models.CharField(blank=True, choices=[('hnew', 'Home | heading 1'), ('hneww', 'Home | Heading 2'), ('hnewww', 'Home | Heading 3'), ('Programme1', 'Home | Programme1'), ('Programme2', 'Home | Programme2'), ('Programme3', 'Home | Programme3'), ('about_us', 'Home | About Us'), ('mission', 'Home | Our Mission'), ('vision', 'Home | Our Vision'), ('Volunteer', 'Home | Volunteer'), ('footer', 'Home | Footer'), ('aboutUs', 'About Us | About Us'), ('our_Programs', 'Programs | Goddess Care Initiative'), ('reach', 'Programs | Our Reach '), ('team1', 'Our Team | Kelly'), ('team2', 'Our Team | Elsie'), ('team3', 'Our Team | Loise')], max_length=100, unique=True),
        ),
    ]
