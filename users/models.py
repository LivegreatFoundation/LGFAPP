from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from taggit.managers import TaggableManager
from html import unescape
from django.utils.html import strip_tags
from shortuuid.django_fields import ShortUUIDField
from pyuploadcare.dj.models import ImageField
from django_prose_editor.fields import ProseEditorField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='Edit your Bio!')
    website = models.CharField(max_length=40)

    def __str__(self):
        return self.user.get_username()
    
class Editpage(models.Model):
    SECTION_CHOICES = [
        ('hnew', 'Home | heading 1'),
        ('hneww', 'Home | Heading 2'),
        ('hnewww', 'Home | Heading 3'),
        ('Programme1', 'Home | Programme1'),
        ('Programme2', 'Home | Programme2'),
        ('Programme3', 'Home | Programme3'),

        ('about_us', 'Home | About Us'),
        ('mission', 'Home | Our Mission'),
        ('vision', 'Home | Our Vision'),
        ('Volunteer', 'Home | Volunteer'),
        ('footer', 'Home | Footer'),
        ('aboutUs', 'About Us | About Us'),
        ('our_Programs', 'Programs | Goddess Care Initiative'),
        ('reach', 'Programs | Our Reach '),
        ('team1', 'Our Team | Kelly'),
        ('team2', 'Our Team | Elsie'),
        ('team3', 'Our Team | Loise'),

    ]

    section_name = models.CharField(max_length=100, choices=SECTION_CHOICES, unique=True, blank=True)
    heading = ProseEditorField(blank=True)
    content = ProseEditorField(blank=True)
    slider_image = ImageField(blank=True, manual_crop="") 
    

    def __str__(self):
        return self.get_section_name_display()
    

class MainProgrames(models.Model):
    SECTION_CHOICES = [
        ('Programme1', 'Programe | Programme1'),
        ('Programme2', 'Programe | Programme2'),
        ('Programme3', 'Programe | Programme3'),
        ('Programme4', 'Programe | Programme4'),

    ]

    programe_name = models.CharField(max_length=100, choices=SECTION_CHOICES, unique=True)
    programe_description = ProseEditorField()
    programe_objective1 = ProseEditorField()
    programe_objective2 = ProseEditorField()
    programe_objective3 = ProseEditorField()
    programe_objective4 = ProseEditorField()


    def __str__(self):
        return self.get_section_name_display()


class SecondSection(models.Model):
    subtitle = ProseEditorField()  # Changed to ProseEditorField
    title = ProseEditorField()     # Changed to ProseEditorField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return strip_tags(self.subtitle)  # Using strip_tags for clean string representation

    class Meta:
        verbose_name = "Second Section"
        verbose_name_plural = "Second Sections"

class SecondSectionIcon(models.Model):
    ICON_CHOICES = [
        ('icon-vegetable', 'Food Icon'),
        ('icon-water-1', 'Water Icon'),
        ('icon-stethoscope', 'Medical Icon'),
        # Add more icon choices as needed
    ]

    icon_class = models.CharField(max_length=50, choices=ICON_CHOICES)
    text = ProseEditorField()      # Changed to ProseEditorField
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{strip_tags(self.text)} - {self.icon_class}"

    class Meta:
        ordering = ['order']
        verbose_name = "Second Section Icon"
        verbose_name_plural = "Second Section Icons"

class SecondSectionBox(models.Model):
    text = ProseEditorField()      # Changed to ProseEditorField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return strip_tags(self.text)

    class Meta:
        verbose_name = "Second Section Box"
        verbose_name_plural = "Second Section Boxes"


# ============================================================================
# ENHANCED CONTENT MANAGEMENT SYSTEM MODELS
# ============================================================================

class PageSection(models.Model):
    """
    Enhanced model for managing different sections of website pages
    """
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Us Page'),
        ('programs', 'Programs Page'),
        ('team', 'Our Team Page'),
        ('contact', 'Contact Page'),
        ('blog', 'Blog Page'),
    ]

    SECTION_TYPE_CHOICES = [
        ('hero', 'Hero Section'),
        ('about', 'About Section'),
        ('mission', 'Mission Section'),
        ('vision', 'Vision Section'),
        ('programs', 'Programs Section'),
        ('team', 'Team Section'),
        ('testimonials', 'Testimonials Section'),
        ('contact', 'Contact Section'),
        ('footer', 'Footer Section'),
        ('custom', 'Custom Section'),
    ]

    # Basic Information
    title = models.CharField(max_length=200, help_text="Section title (for admin reference)")
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, help_text="Which page this section belongs to")
    section_type = models.CharField(max_length=50, choices=SECTION_TYPE_CHOICES, help_text="Type of section")
    slug = models.SlugField(unique=True, help_text="Unique identifier for this section")

    # Content Fields
    heading = models.CharField(max_length=300, blank=True, help_text="Main heading for this section")
    subheading = models.CharField(max_length=500, blank=True, help_text="Subheading or tagline")
    content = ProseEditorField(blank=True, help_text="Main content with rich text editing")

    # Media
    background_image = models.ImageField(upload_to='sections/backgrounds/', blank=True, null=True, help_text="Background image for this section")
    featured_image = models.ImageField(upload_to='sections/featured/', blank=True, null=True, help_text="Featured image for this section")

    # Layout and Display
    is_active = models.BooleanField(default=True, help_text="Show this section on the website")
    order = models.IntegerField(default=0, help_text="Order of appearance on the page (lower numbers appear first)")
    css_classes = models.CharField(max_length=200, blank=True, help_text="Additional CSS classes for styling")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page', 'order']
        verbose_name = "Page Section"
        verbose_name_plural = "Page Sections"
        unique_together = ['page', 'section_type', 'order']

    def __str__(self):
        return f"{self.get_page_display()} - {self.title}"


class ContentBlock(models.Model):
    """
    Flexible content blocks that can be added to any page section
    """
    BLOCK_TYPE_CHOICES = [
        ('text', 'Text Block'),
        ('image', 'Image Block'),
        ('video', 'Video Block'),
        ('quote', 'Quote Block'),
        ('stats', 'Statistics Block'),
        ('cta', 'Call to Action Block'),
        ('gallery', 'Image Gallery'),
        ('contact_form', 'Contact Form'),
    ]

    # Basic Information
    title = models.CharField(max_length=200, help_text="Block title (for admin reference)")
    block_type = models.CharField(max_length=50, choices=BLOCK_TYPE_CHOICES)
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE, related_name='content_blocks')

    # Content Fields
    heading = models.CharField(max_length=300, blank=True)
    content = ProseEditorField(blank=True)

    # Media
    image = models.ImageField(upload_to='content_blocks/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="YouTube or Vimeo URL")

    # Additional Fields for specific block types
    button_text = models.CharField(max_length=100, blank=True, help_text="For CTA blocks")
    button_url = models.URLField(blank=True, help_text="For CTA blocks")
    quote_author = models.CharField(max_length=200, blank=True, help_text="For quote blocks")
    stat_number = models.CharField(max_length=50, blank=True, help_text="For statistics blocks")
    stat_label = models.CharField(max_length=100, blank=True, help_text="For statistics blocks")

    # Layout
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    css_classes = models.CharField(max_length=200, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['section', 'order']
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __str__(self):
        return f"{self.section.title} - {self.title}"


class TeamMember(models.Model):
    """
    Enhanced model for team members
    """
    # Basic Information
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, help_text="Job title or role")
    bio = ProseEditorField(help_text="Biography with rich text editing")

    # Contact Information
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    # Media
    photo = models.ImageField(upload_to='team/', help_text="Professional headshot")

    # Display Settings
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on team page")
    order = models.IntegerField(default=0, help_text="Display order")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.position}"


class Program(models.Model):
    """
    Enhanced model for foundation programs
    """
    # Basic Information
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=500, help_text="Brief description for cards and previews")
    full_description = ProseEditorField(help_text="Detailed description with rich text editing")

    # Media
    featured_image = models.ImageField(upload_to='programs/', help_text="Main program image")

    # Program Details
    objectives = ProseEditorField(blank=True, help_text="Program objectives and goals")
    target_audience = models.CharField(max_length=300, blank=True, help_text="Who this program serves")
    location = models.CharField(max_length=200, blank=True, help_text="Where the program operates")

    # Impact and Statistics
    beneficiaries_count = models.PositiveIntegerField(default=0, help_text="Number of people helped")
    start_date = models.DateField(blank=True, null=True, help_text="When the program started")

    # Display Settings
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on programs page")
    order = models.IntegerField(default=0, help_text="Display order")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return self.name


class ProgramImage(models.Model):
    """
    Images for program galleries
    """
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='programs/gallery/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Program Image"
        verbose_name_plural = "Program Images"

    def __str__(self):
        return f"{self.program.name} - Image {self.id}"


class WebsiteContent(models.Model):
    """
    Improved page content management system replacing the legacy Editpage model
    """
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Us Page'),
        ('programs', 'Programs Page'),
        ('team', 'Our Team Page'),
        ('contact', 'Contact Us Page'),
    ]

    CONTENT_TYPE_CHOICES = [
        # Home Page Content
        ('home_hero_main', 'Home: Main Hero Section'),
        ('home_hero_secondary', 'Home: Secondary Hero Section'),
        ('home_hero_tertiary', 'Home: Third Hero Section'),
        ('home_about_preview', 'Home: About Us Preview'),
        ('home_mission_statement', 'Home: Mission Statement'),
        ('home_vision_statement', 'Home: Vision Statement'),
        ('home_volunteer_section', 'Home: Volunteer Call-to-Action'),
        ('home_program_1', 'Home: Featured Program 1'),
        ('home_program_2', 'Home: Featured Program 2'),
        ('home_program_3', 'Home: Featured Program 3'),

        # About Page Content
        ('about_main_content', 'About: Main About Us Content'),
        ('about_mission_detailed', 'About: Detailed Mission Statement'),
        ('about_vision_detailed', 'About: Detailed Vision Statement'),
        ('about_history', 'About: Our History'),
        ('about_values', 'About: Our Values'),

        # Programs Page Content
        ('programs_overview', 'Programs: Overview Section'),
        ('programs_goddess_care', 'Programs: Goddess Care Initiative'),
        ('programs_reach', 'Programs: Our Reach'),
        ('programs_impact', 'Programs: Impact Statistics'),

        # Team Page Content
        ('team_kelly', 'Team: Kelly Wanjiku Profile'),
        ('team_elsie', 'Team: Elsie Muthoni Profile'),
        ('team_loise', 'Team: Loise Njeri Profile'),
        ('team_overview', 'Team: Team Overview'),

        # Contact Page Content
        ('contact_main', 'Contact: Main Contact Information'),
        ('contact_office', 'Contact: Office Details'),
        ('contact_form_intro', 'Contact: Contact Form Introduction'),

        # Global Content
        ('footer_content', 'Global: Footer Content'),
        ('header_announcement', 'Global: Header Announcement'),
    ]

    # Basic Information
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, help_text="Which page this content appears on")
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPE_CHOICES, unique=True, help_text="Specific section of the page")
    title = models.CharField(max_length=200, help_text="Internal title for admin reference")

    # Content Fields
    heading = ProseEditorField(blank=True, help_text="Main heading that appears on the website")
    content = ProseEditorField(blank=True, help_text="Main content with rich text formatting")
    image = models.ImageField(upload_to='website_content/', blank=True, null=True, help_text="Image for this content section")

    # Display Settings
    is_active = models.BooleanField(default=True, help_text="Show this content on the website")
    display_order = models.IntegerField(default=0, help_text="Order of appearance (lower numbers appear first)")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="Last person to edit this content")

    class Meta:
        ordering = ['page', 'display_order', 'content_type']
        verbose_name = "Website Content"
        verbose_name_plural = "Website Content"

    def __str__(self):
        return f"{self.get_page_display()} - {self.get_content_type_display()}"

    def get_preview_text(self):
        """Get a preview of the content for admin display"""
        if self.content:
            from django.utils.html import strip_tags
            preview = strip_tags(self.content)[:100]
            return f"{preview}..." if len(preview) == 100 else preview
        return "No content"

    def save(self, *args, **kwargs):
        # Auto-generate title if not provided
        if not self.title:
            self.title = self.get_content_type_display()
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """
    Global site settings that can be edited through admin
    """
    # Site Identity
    site_name = models.CharField(max_length=200, default="Live Great Foundation")
    tagline = models.CharField(max_length=300, blank=True, help_text="Site tagline or motto")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)

    # Contact Information
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    # Social Media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # SEO Settings
    meta_description = models.TextField(max_length=160, blank=True, help_text="Default meta description for SEO")
    meta_keywords = models.CharField(max_length=300, blank=True, help_text="Default meta keywords for SEO")

    # Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True, help_text="Google Analytics tracking ID")
    facebook_pixel_id = models.CharField(max_length=50, blank=True, help_text="Facebook Pixel ID")

    # Footer Content
    footer_text = ProseEditorField(blank=True, help_text="Footer content with rich text editing")
    copyright_text = models.CharField(max_length=200, blank=True, help_text="Copyright notice")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Site Settings - {self.site_name}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError("Only one SiteSettings instance is allowed")
        super().save(*args, **kwargs)
