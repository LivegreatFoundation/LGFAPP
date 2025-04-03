# Generated by Django 3.2.20 on 2025-04-03 00:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='StaticContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(choices=[('about_us', 'About Us'), ('mission', 'Our Mission'), ('vision', 'Vision')], max_length=100, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=1000)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField(max_length=10000)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('in_review', 'In Review'), ('published', 'Published')], default='in_review', max_length=100)),
                ('featured', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogapp.post')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
