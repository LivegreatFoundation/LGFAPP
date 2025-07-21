"""
Template tags for easy access to website content
"""

from django import template
from django.utils.safestring import mark_safe
from users.models import WebsiteContent

register = template.Library()


@register.simple_tag
def get_content(content_type, field='content', default=''):
    """
    Get website content by content type
    
    Usage:
    {% get_content 'home_hero_main' 'heading' %}
    {% get_content 'home_hero_main' 'content' %}
    {% get_content 'home_hero_main' 'image' %}
    """
    try:
        content = WebsiteContent.objects.get(content_type=content_type, is_active=True)
        value = getattr(content, field, default)
        
        # Return safe HTML for content fields
        if field in ['content', 'heading'] and value:
            return mark_safe(value)
        
        return value or default
    except WebsiteContent.DoesNotExist:
        return default


@register.simple_tag
def get_content_object(content_type):
    """
    Get the full website content object
    
    Usage:
    {% get_content_object 'home_hero_main' as hero_content %}
    {% if hero_content %}
        <h1>{{ hero_content.heading|safe }}</h1>
        <div>{{ hero_content.content|safe }}</div>
        {% if hero_content.image %}
            <img src="{{ hero_content.image.url }}" alt="{{ hero_content.heading }}">
        {% endif %}
    {% endif %}
    """
    try:
        return WebsiteContent.objects.get(content_type=content_type, is_active=True)
    except WebsiteContent.DoesNotExist:
        return None


@register.inclusion_tag('includes/content_section.html')
def render_content_section(content_type, css_class='', wrapper_tag='div'):
    """
    Render a complete content section with heading, content, and image
    
    Usage:
    {% render_content_section 'home_hero_main' 'hero-section' 'section' %}
    """
    try:
        content = WebsiteContent.objects.get(content_type=content_type, is_active=True)
        return {
            'content': content,
            'css_class': css_class,
            'wrapper_tag': wrapper_tag,
        }
    except WebsiteContent.DoesNotExist:
        return {
            'content': None,
            'css_class': css_class,
            'wrapper_tag': wrapper_tag,
        }


@register.simple_tag
def get_page_content(page, order_by='display_order'):
    """
    Get all content for a specific page
    
    Usage:
    {% get_page_content 'home' as home_content %}
    {% for content in home_content %}
        <div class="content-section">
            <h2>{{ content.heading|safe }}</h2>
            <div>{{ content.content|safe }}</div>
        </div>
    {% endfor %}
    """
    return WebsiteContent.objects.filter(
        page=page, 
        is_active=True
    ).order_by(order_by)


@register.filter
def has_content(content_type):
    """
    Check if content exists and is active
    
    Usage:
    {% if 'home_hero_main'|has_content %}
        <!-- Show content -->
    {% endif %}
    """
    return WebsiteContent.objects.filter(
        content_type=content_type, 
        is_active=True
    ).exists()


# Legacy compatibility tags for gradual migration
@register.simple_tag
def legacy_content(section_name, field='content', default=''):
    """
    Legacy compatibility tag for old Editpage model
    This helps during the transition period
    
    Usage:
    {% legacy_content 'hnew' 'heading' %}
    """
    # Mapping from old section names to new content types
    legacy_mapping = {
        'hnew': 'home_hero_main',
        'hneww': 'home_hero_secondary',
        'hnewww': 'home_hero_tertiary',
        'Programme1': 'home_program_1',
        'Programme2': 'home_program_2',
        'Programme3': 'home_program_3',
        'about_us': 'home_about_preview',
        'mission': 'home_mission_statement',
        'vision': 'home_vision_statement',
        'Volunteer': 'home_volunteer_section',
        'footer': 'footer_content',
        'aboutUs': 'about_main_content',
        'our_Programs': 'programs_goddess_care',
        'reach': 'programs_reach',
        'team1': 'team_kelly',
        'team2': 'team_elsie',
        'team3': 'team_loise',
    }
    
    # Try to get content from new system first
    new_content_type = legacy_mapping.get(section_name)
    if new_content_type:
        return get_content(new_content_type, field, default)
    
    # Fallback to old system if needed
    try:
        from users.models import Editpage
        content = Editpage.objects.get(section_name=section_name)
        value = getattr(content, field, default)
        
        if field in ['content', 'heading'] and value:
            return mark_safe(value)
        
        return value or default
    except:
        return default


# Example usage in templates:
"""
<!-- Load the template tags -->
{% load website_content %}

<!-- Get specific content fields -->
<h1>{% get_content 'home_hero_main' 'heading' %}</h1>
<p>{% get_content 'home_hero_main' 'content' %}</p>

<!-- Get full content object -->
{% get_content_object 'home_hero_main' as hero %}
{% if hero %}
    <div class="hero-section">
        <h1>{{ hero.heading|safe }}</h1>
        <div>{{ hero.content|safe }}</div>
        {% if hero.image %}
            <img src="{{ hero.image.url }}" alt="{{ hero.heading }}">
        {% endif %}
    </div>
{% endif %}

<!-- Render complete content section -->
{% render_content_section 'home_hero_main' 'hero-section' 'section' %}

<!-- Get all content for a page -->
{% get_page_content 'home' as home_content %}
{% for content in home_content %}
    <div class="content-item">
        <h2>{{ content.heading|safe }}</h2>
        <div>{{ content.content|safe }}</div>
    </div>
{% endfor %}

<!-- Check if content exists -->
{% if 'home_hero_main'|has_content %}
    <div class="hero-section">
        {% get_content 'home_hero_main' 'content' %}
    </div>
{% endif %}

<!-- Legacy compatibility (for gradual migration) -->
<h1>{% legacy_content 'hnew' 'heading' %}</h1>
"""
