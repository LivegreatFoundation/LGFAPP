from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from taggit.managers import TaggableManager
from html import unescape
from django.utils.html import strip_tags
from shortuuid.django_fields import ShortUUIDField
from pyuploadcare.dj.models import ImageField
from ckeditor.fields import RichTextField


BLOG_PUBLISH_STATUS = (
	("draft", "draft"),
	("in_review", "In Review"),
	("published", "Published"),
)



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title 
        
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    Author = models.CharField(max_length=1000)
    image = ImageField(blank=True, null=True, manual_crop="16:9")
    title = models.CharField(max_length=1000)
    content = RichTextField(max_length=10000)
    slug = models.SlugField(unique=True, blank=True)  # Add this if not already present
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    status = models.CharField(choices=BLOG_PUBLISH_STATUS, max_length=100, default="in_review")
    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    pid = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"
        ordering = ['-date']
        
    def save(self, *args, **kwargs):
        # Set Author name if blank
        if not self.Author and self.user:
            self.Author = f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username

        # If no user is set, use the default admin user
        if not self.user:
            default_user = User.objects.filter(is_superuser=True).first()
            if default_user:
                self.user = default_user
                if not self.Author:
                    self.Author = default_user.username

        # Generate slug if not exists
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title[0:10]

    def get_read_time(self):
        string = self.content + unescape(strip_tags(self.content))
        total_words = len((string).split())
        return round(total_words / 200)

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=1000)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comment[0:20]
    


class StaticContent(models.Model):
    SECTION_CHOICES = [
        ('about_us', 'About Us'),
        ('mission', 'Our Mission'),
        ('vision', 'Vision'),
    ]

    section_name = models.CharField(max_length=100, choices=SECTION_CHOICES, unique=True)
    content = RichTextField()

    def __str__(self):
        return self.get_section_name_display()