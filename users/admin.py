from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from . models import (
    Profile, Editpage, SecondSection, SecondSectionIcon, SecondSectionBox,
    PageSection, ContentBlock, TeamMember, Program, ProgramImage, SiteSettings,
    WebsiteContent
)


# ============================================================================
# ENHANCED ADMIN CLASSES FOR CONTENT MANAGEMENT
# ============================================================================

class ContentBlockInline(StackedInline):
    """Inline admin for content blocks within page sections"""
    model = ContentBlock
    extra = 0
    fields = (
        ('title', 'block_type', 'order'),
        'heading',
        'content',
        ('image', 'video_url'),
        ('button_text', 'button_url'),
        ('quote_author', 'stat_number', 'stat_label'),
        ('is_active', 'css_classes'),
    )
    classes = ['collapse']


@admin.register(PageSection)
class PageSectionAdmin(ModelAdmin):
    """Enhanced admin for page sections with inline content blocks"""

    list_display = ['title', 'page', 'section_type', 'order', 'is_active', 'preview_button']
    list_filter = ['page', 'section_type', 'is_active', 'created_at']
    search_fields = ['title', 'heading', 'content']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'page', 'section_type', 'slug')
        }),
        ('Content', {
            'fields': ('heading', 'subheading', 'content'),
            'classes': ('wide',)
        }),
        ('Media', {
            'fields': ('background_image', 'featured_image'),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order', 'css_classes'),
            'classes': ('collapse',)
        }),
    )

    inlines = [ContentBlockInline]

    def preview_button(self, obj):
        """Add a preview button for each section"""
        if obj.pk:
            return format_html(
                '<a href="{}#section-{}" target="_blank" class="button">👁️ Preview</a>',
                '/',  # You can customize this URL
                obj.slug
            )
        return "Save to preview"
    preview_button.short_description = "Preview"

    class Media:
        css = {
            'all': ('admin/css/enhanced_admin.css',)
        }


@admin.register(ContentBlock)
class ContentBlockAdmin(ModelAdmin):
    """Admin for individual content blocks"""

    list_display = ['title', 'section', 'block_type', 'order', 'is_active']
    list_filter = ['block_type', 'section__page', 'is_active']
    search_fields = ['title', 'heading', 'content']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'section', 'block_type', 'order')
        }),
        ('Content', {
            'fields': ('heading', 'content'),
            'classes': ('wide',)
        }),
        ('Media', {
            'fields': ('image', 'video_url'),
            'classes': ('collapse',)
        }),
        ('Call to Action', {
            'fields': ('button_text', 'button_url'),
            'classes': ('collapse',),
            'description': 'For CTA blocks only'
        }),
        ('Quote Block', {
            'fields': ('quote_author',),
            'classes': ('collapse',),
            'description': 'For quote blocks only'
        }),
        ('Statistics Block', {
            'fields': ('stat_number', 'stat_label'),
            'classes': ('collapse',),
            'description': 'For statistics blocks only'
        }),
        ('Display Settings', {
            'fields': ('is_active', 'css_classes'),
            'classes': ('collapse',)
        }),
    )


class ProgramImageInline(TabularInline):
    """Inline admin for program images"""
    model = ProgramImage
    extra = 0
    fields = ('image', 'caption', 'order')


@admin.register(Program)
class ProgramAdmin(ModelAdmin):
    """Enhanced admin for programs"""

    list_display = ['name', 'target_audience', 'beneficiaries_count', 'is_featured', 'is_active', 'order']
    list_filter = ['is_featured', 'is_active', 'start_date']
    search_fields = ['name', 'short_description', 'target_audience']
    list_editable = ['is_featured', 'is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'short_description')
        }),
        ('Detailed Content', {
            'fields': ('full_description', 'objectives'),
            'classes': ('wide',)
        }),
        ('Program Details', {
            'fields': ('target_audience', 'location', 'start_date', 'beneficiaries_count'),
            'classes': ('collapse',)
        }),
        ('Media', {
            'fields': ('featured_image',),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order'),
            'classes': ('collapse',)
        }),
    )

    inlines = [ProgramImageInline]


@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    """Enhanced admin for team members"""

    list_display = ['name', 'position', 'email', 'is_featured', 'is_active', 'order']
    list_filter = ['is_featured', 'is_active', 'position']
    search_fields = ['name', 'position', 'bio']
    list_editable = ['is_featured', 'is_active', 'order']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone'),
            'classes': ('collapse',)
        }),
        ('Social Media', {
            'fields': ('linkedin_url', 'twitter_url'),
            'classes': ('collapse',)
        }),
        ('Media', {
            'fields': ('photo',),
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    """Admin for global site settings"""

    fieldsets = (
        ('Site Identity', {
            'fields': ('site_name', 'tagline', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address'),
            'classes': ('collapse',)
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url'),
            'classes': ('collapse',)
        }),
        ('SEO Settings', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Analytics', {
            'fields': ('google_analytics_id', 'facebook_pixel_id'),
            'classes': ('collapse',)
        }),
        ('Footer', {
            'fields': ('footer_text', 'copyright_text'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of site settings
        return False


# ============================================================================
# LEGACY ADMIN CLASSES (Enhanced)
# ============================================================================

class EditpageAdmin(ModelAdmin):
    """Enhanced admin for legacy Editpage model"""
    list_display = ('section_name', 'get_content_preview', 'slider_image_preview')
    search_fields = ['section_name', 'heading', 'content']
    list_filter = ['section_name']

    fieldsets = (
        ('Section Information', {
            'fields': ('section_name',)
        }),
        ('Content', {
            'fields': ('heading', 'content'),
            'classes': ('wide',)
        }),
        ('Media', {
            'fields': ('slider_image',),
        }),
    )

    def get_content_preview(self, obj):
        """Show a preview of the content"""
        if obj.content:
            from django.utils.html import strip_tags
            preview = strip_tags(obj.content)[:100]
            return f"{preview}..." if len(preview) == 100 else preview
        return "No content"
    get_content_preview.short_description = "Content Preview"

    def slider_image_preview(self, obj):
        """Show image preview"""
        if obj.slider_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.slider_image.cdn_url)
        return "No image"
    slider_image_preview.short_description = "Image"


# ============================================================================
# IMPROVED WEBSITE CONTENT ADMIN
# ============================================================================

@admin.register(WebsiteContent)
class WebsiteContentAdmin(ModelAdmin):
    """
    User-friendly admin interface for website content management
    """
    list_display = (
        'content_type_display',
        'page_display',
        'heading_preview',
        'content_preview',
        'image_preview',
        'is_active',
        'display_order',
        'last_updated'
    )

    list_filter = (
        'page',
        'is_active',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'title',
        'heading',
        'content',
        'content_type'
    )

    list_editable = ('is_active', 'display_order')

    fieldsets = (
        ('📍 Content Location', {
            'fields': ('page', 'content_type', 'title'),
            'description': 'Specify where this content appears on your website'
        }),
        ('📝 Content', {
            'fields': ('heading', 'content', 'image'),
            'description': 'The actual content that visitors will see'
        }),
        ('⚙️ Display Settings', {
            'fields': ('is_active', 'display_order'),
            'description': 'Control how and when this content is shown'
        }),
        ('📊 Information', {
            'fields': ('created_at', 'updated_at', 'last_edited_by'),
            'classes': ('collapse',),
            'description': 'Tracking information'
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'last_edited_by')

    ordering = ('page', 'display_order', 'content_type')

    def content_type_display(self, obj):
        """Display content type with icon"""
        icons = {
            'home': '🏠',
            'about': 'ℹ️',
            'programs': '📋',
            'team': '👥',
            'contact': '📞'
        }
        icon = icons.get(obj.page, '📄')
        return format_html(
            '<span style="font-weight: bold;">{} {}</span>',
            icon,
            obj.get_content_type_display()
        )
    content_type_display.short_description = "Content Section"
    content_type_display.admin_order_field = 'content_type'

    def page_display(self, obj):
        """Display page with icon"""
        return format_html(
            '<span style="background: #e3f2fd; padding: 2px 8px; border-radius: 12px; font-size: 12px;">{}</span>',
            obj.get_page_display()
        )
    page_display.short_description = "Page"
    page_display.admin_order_field = 'page'

    def heading_preview(self, obj):
        """Show preview of heading"""
        if obj.heading:
            from django.utils.html import strip_tags
            preview = strip_tags(obj.heading)[:50]
            return f"{preview}..." if len(preview) == 50 else preview
        return "No heading"
    heading_preview.short_description = "Heading"

    def content_preview(self, obj):
        """Show preview of content"""
        return obj.get_preview_text()
    content_preview.short_description = "Content Preview"

    def image_preview(self, obj):
        """Show small image preview"""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 40px; height: 40px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = "Image"

    def last_updated(self, obj):
        """Show last update time"""
        return obj.updated_at.strftime("%b %d, %Y")
    last_updated.short_description = "Last Updated"
    last_updated.admin_order_field = 'updated_at'

    def save_model(self, request, obj, form, change):
        """Track who last edited the content"""
        obj.last_edited_by = request.user
        super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('admin/css/website_content.css',)
        }


# ============================================================================
# LEGACY ADMIN REGISTRATIONS
# ============================================================================

# Register models
admin.site.register(Profile)
admin.site.register(Editpage, EditpageAdmin)
admin.site.register(SecondSection)
admin.site.register(SecondSectionIcon)
admin.site.register(SecondSectionBox)
admin.site.register(ProgramImage)