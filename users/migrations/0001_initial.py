# Generated by Django 3.2.20 on 2025-04-02 21:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Editpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(blank=True, choices=[('hnew', 'Home | heading 1'), ('hneww', 'Home | Heading 2'), ('hnewww', 'Home | Heading 3'), ('Programme1', 'Home | Programme1'), ('Programme2', 'Home | Programme2'), ('Programme3', 'Home | Programme3'), ('about_us', 'Home | About Us'), ('mission', 'Home | Our Mission'), ('vision', 'Home | Our Vision'), ('Volunteer', 'Home | Volunteer'), ('footer', 'Home | Footer'), ('aboutUs', 'About Us | About Us'), ('our_Programs', 'Programs | Goddess Care Initiative'), ('reach', 'Programs | Our Reach '), ('team1', 'Our Team | Kelly'), ('team2', 'Our Team | Elsie'), ('team3', 'Our Team | Loise')], max_length=100, unique=True)),
                ('heading', ckeditor.fields.RichTextField(blank=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('slider_image', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainProgrames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programe_name', models.CharField(choices=[('Programme1', 'Programe | Programme1'), ('Programme2', 'Programe | Programme2'), ('Programme3', 'Programe | Programme3'), ('Programme4', 'Programe | Programme4')], max_length=100, unique=True)),
                ('programe_description', ckeditor.fields.RichTextField()),
                ('programe_objective1', ckeditor.fields.RichTextField()),
                ('programe_objective2', ckeditor.fields.RichTextField()),
                ('programe_objective3', ckeditor.fields.RichTextField()),
                ('programe_objective4', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', ckeditor.fields.RichTextField()),
                ('title', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Second Section',
                'verbose_name_plural': 'Second Sections',
            },
        ),
        migrations.CreateModel(
            name='SecondSectionBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Second Section Box',
                'verbose_name_plural': 'Second Section Boxes',
            },
        ),
        migrations.CreateModel(
            name='SecondSectionIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class', models.CharField(choices=[('icon-vegetable', 'Food Icon'), ('icon-water-1', 'Water Icon'), ('icon-stethoscope', 'Medical Icon')], max_length=50)),
                ('text', ckeditor.fields.RichTextField()),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Second Section Icon',
                'verbose_name_plural': 'Second Section Icons',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField(default='Edit your Bio!')),
                ('website', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
