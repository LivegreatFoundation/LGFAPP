from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blogapp.models import Category
from taggit.models import Tag


class Command(BaseCommand):
    help = 'Populate default categories and tags for the Live Great Foundation blog'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing categories and tags before adding new ones',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing categories and tags...')
            Category.objects.all().delete()
            Tag.objects.all().delete()
            self.stdout.write(self.style.WARNING('Cleared existing data.'))

        # Default categories for Live Great Foundation
        categories_data = [
            {
                'title': 'Health & Wellness',
                'description': 'Articles about health, nutrition, and wellness programs'
            },
            {
                'title': 'Education',
                'description': 'Educational content and literacy programs'
            },
            {
                'title': 'Community Development',
                'description': 'Community building and development initiatives'
            },
            {
                'title': 'Women Empowerment',
                'description': 'Programs and stories about empowering women and girls'
            },
            {
                'title': 'Environmental Sustainability',
                'description': 'Environmental conservation and sustainability efforts'
            },
            {
                'title': 'Youth Programs',
                'description': 'Programs and activities for young people'
            },
            {
                'title': 'Success Stories',
                'description': 'Inspiring stories from our community'
            },
            {
                'title': 'Events & News',
                'description': 'Foundation events, news, and announcements'
            },
            {
                'title': 'Partnerships',
                'description': 'Collaborations and partnership announcements'
            },
            {
                'title': 'Fundraising',
                'description': 'Fundraising campaigns and donation drives'
            }
        ]

        # Create categories
        self.stdout.write('Creating categories...')
        created_categories = 0
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                title=cat_data['title'],
                defaults={
                    'slug': slugify(cat_data['title']),
                    'active': True
                }
            )
            if created:
                created_categories += 1
                self.stdout.write(f'  ✓ Created category: {category.title}')
            else:
                self.stdout.write(f'  - Category already exists: {category.title}')

        # Default tags for Live Great Foundation
        tags_data = [
            # Health & Wellness tags
            'nutrition', 'healthcare', 'mental-health', 'wellness', 'fitness',
            'maternal-health', 'child-health', 'hygiene', 'clean-water',
            
            # Education tags
            'literacy', 'education', 'learning', 'skills-training', 'vocational-training',
            'adult-education', 'early-childhood', 'scholarships', 'books',
            
            # Community tags
            'community', 'development', 'empowerment', 'leadership', 'capacity-building',
            'social-impact', 'grassroots', 'local-initiatives', 'volunteer',
            
            # Women & Gender tags
            'women-empowerment', 'gender-equality', 'girls-education', 'women-leadership',
            'economic-empowerment', 'reproductive-health', 'gender-based-violence',
            
            # Environment tags
            'environment', 'sustainability', 'climate-change', 'conservation',
            'renewable-energy', 'waste-management', 'green-initiatives',
            
            # Youth tags
            'youth', 'children', 'mentorship', 'youth-leadership', 'sports',
            'arts', 'creativity', 'life-skills',
            
            # Program tags
            'training', 'workshop', 'seminar', 'conference', 'outreach',
            'awareness', 'campaign', 'advocacy', 'research',
            
            # Impact tags
            'success-story', 'testimonial', 'impact', 'transformation',
            'achievement', 'milestone', 'progress', 'results',
            
            # Partnership tags
            'partnership', 'collaboration', 'donor', 'sponsor', 'volunteer',
            'government', 'ngo', 'private-sector', 'international',
            
            # Location tags (Kenya-specific)
            'kenya', 'nairobi', 'rural', 'urban', 'africa', 'east-africa',
            
            # Foundation specific
            'live-great-foundation', 'lgf', 'mission', 'vision', 'values',
            'annual-report', 'newsletter', 'update'
        ]

        # Create tags
        self.stdout.write('Creating tags...')
        created_tags = 0
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            if created:
                created_tags += 1
                self.stdout.write(f'  ✓ Created tag: {tag.name}')
            else:
                self.stdout.write(f'  - Tag already exists: {tag.name}')

        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Successfully populated blog data:\n'
            f'  • {created_categories} new categories created\n'
            f'  • {created_tags} new tags created\n'
            f'  • Total categories: {Category.objects.count()}\n'
            f'  • Total tags: {Tag.objects.count()}'
        ))
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            'Blog categories and tags are now ready for use!\n'
            'You can manage them through the Django admin interface.'
        ))
