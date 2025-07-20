from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.utils.html import format_html
from django.conf import settings
import os

from blogapp.models import Post, Comment, Category, StaticContent
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from unfold.admin import ModelAdmin
from taggit.models import Tag


class PostResource(resources.ModelResource):
    """Custom resource for importing blog posts with enhanced functionality"""

    # Custom field mappings
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'title')
    )

    featured = fields.Field(
        column_name='featured',
        attribute='featured',
        widget=BooleanWidget()
    )

    trending = fields.Field(
        column_name='trending',
        attribute='trending',
        widget=BooleanWidget()
    )

    tags = fields.Field(
        column_name='tags',
        attribute='tags',
        readonly=False
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'Author', 'category', 'status', 'tags', 'featured', 'trending')
        export_order = ('title', 'content', 'Author', 'category', 'status', 'tags', 'featured', 'trending')
        import_id_fields = ('title',)  # Use title as unique identifier
        skip_unchanged = True
        report_skipped = True

    def before_import_row(self, row, **kwargs):
        """Process row before import - handle defaults and validation"""
        # Set default status to published if not specified
        if not row.get('status'):
            row['status'] = 'published'

        # Set default boolean values
        if not row.get('featured'):
            row['featured'] = 'FALSE'
        if not row.get('trending'):
            row['trending'] = 'FALSE'

        # Clean up boolean values
        row['featured'] = str(row.get('featured', 'FALSE')).upper()
        row['trending'] = str(row.get('trending', 'FALSE')).upper()

        return super().before_import_row(row, **kwargs)

    def after_save_instance(self, instance, using_transactions, dry_run):
        """Handle tags after saving the instance"""
        if not dry_run and hasattr(instance, '_tags_cache'):
            # Clear existing tags
            instance.tags.clear()

            # Add new tags
            tag_names = instance._tags_cache
            if tag_names:
                for tag_name in tag_names:
                    tag_name = tag_name.strip()
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        instance.tags.add(tag)

        return super().after_save_instance(instance, using_transactions, dry_run)

    def import_field(self, field, obj, data, is_m2m=False):
        """Custom field import handling"""
        if field.column_name == 'tags':
            # Handle comma-separated tags
            tags_string = data.get('tags', '')
            if tags_string:
                tag_names = [tag.strip() for tag in tags_string.split(',') if tag.strip()]
                obj._tags_cache = tag_names
            return

        return super().import_field(field, obj, data, is_m2m)

class StaticContentAdmin(ModelAdmin):
    list_display = ('section_name', 'content')
    search_fields = ['section_name']

class ArticleAdmin(ImportExportModelAdmin, ModelAdmin):
    resource_class = PostResource
    search_fields = ['title']
    list_display = ('title', 'status', 'category', 'user', 'featured', 'trending')
    list_editable = ['status', 'category']
    list_filter = ('category', 'status', 'featured', 'trending', 'date')
    readonly_fields = ('views', 'date')

    fieldsets = (
        ('Content', {
            'fields': ('title', 'content', 'image')
        }),
        ('Meta', {
            'fields': ('Author', 'category', 'tags')
        }),
        ('Settings', {
            'fields': ('status', 'featured', 'trending')
        }),
        ('Statistics', {
            'fields': ('views', 'date'),
            'classes': ('collapse',)
        }),
    )

    # Import/Export settings
    import_template_name = 'admin/import_export/import.html'
    change_form_template = 'admin/blogapp/post/change_form.html'
    add_form_template = 'admin/blogapp/post/change_form.html'

    def get_urls(self):
        """Add custom URLs for template download"""
        urls = super().get_urls()
        custom_urls = [
            path('download-template/', self.download_template, name='blogapp_post_download_template'),
        ]
        return custom_urls + urls

    def download_template(self, request):
        """Download the Excel import template"""
        template_path = os.path.join(settings.BASE_DIR, 'static', 'admin', 'templates', 'blog_post_import_template.xlsx')

        if os.path.exists(template_path):
            with open(template_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="blog_post_import_template.xlsx"'
                return response
        else:
            # If template doesn't exist, create it on the fly
            from django.contrib import messages
            messages.error(request, 'Import template not found. Please contact administrator.')
            return self.changelist_view(request)



    def changelist_view(self, request, extra_context=None):
        """Add template download link to changelist"""
        extra_context = extra_context or {}
        extra_context['template_download_url'] = 'download-template/'
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'user')

class CategoryAdmin(ImportExportModelAdmin, ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'active')

class CommentAdmin(ImportExportModelAdmin, ModelAdmin):
    list_display = ('post', 'full_name', 'email', 'active', 'date')
    list_editable = ('active',)
    list_filter = ('active', 'date')
    search_fields = ['comment', 'full_name', 'email']

admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StaticContent, StaticContentAdmin)