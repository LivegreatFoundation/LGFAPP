"""
Management command to set up sample website content using the new WebsiteContent model
"""

from django.core.management.base import BaseCommand
from users.models import WebsiteContent


class Command(BaseCommand):
    help = 'Set up sample website content using the new WebsiteContent model'

    def handle(self, *args, **options):
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🚀 Setting up Website Content'))
        self.stdout.write('=' * 60)

        # Sample content data
        content_data = [
            # Home Page Content
            {
                'page': 'home',
                'content_type': 'home_hero_main',
                'title': 'Main Hero Section',
                'heading': 'Empowering Communities, Transforming Lives',
                'content': '<p>Welcome to Live Great Foundation, where we believe every community has the potential for greatness. Through our comprehensive programs and partnerships, we work hand-in-hand with local communities to create lasting positive change across Kenya.</p>',
                'display_order': 1,
            },
            {
                'page': 'home',
                'content_type': 'home_hero_secondary',
                'title': 'Secondary Hero Section',
                'heading': 'Building Stronger Communities',
                'content': '<p>Our mission is to empower communities through education, healthcare, environmental conservation, and economic opportunities that create sustainable development.</p>',
                'display_order': 2,
            },
            {
                'page': 'home',
                'content_type': 'home_about_preview',
                'title': 'About Us Preview',
                'heading': 'Who We Are',
                'content': '<p>Live Great Foundation is a nonprofit organization dedicated to creating positive change in communities across Kenya. We focus on sustainable development through education, health, environmental conservation, and economic empowerment programs.</p>',
                'display_order': 3,
            },
            {
                'page': 'home',
                'content_type': 'home_mission_statement',
                'title': 'Mission Statement',
                'heading': 'Our Mission',
                'content': '<p>To empower communities across Kenya by providing access to quality education, healthcare, environmental conservation programs, and economic opportunities that create sustainable positive change.</p>',
                'display_order': 4,
            },
            {
                'page': 'home',
                'content_type': 'home_vision_statement',
                'title': 'Vision Statement',
                'heading': 'Our Vision',
                'content': '<p>A Kenya where every community thrives with access to quality education, healthcare, clean environment, and economic opportunities for all.</p>',
                'display_order': 5,
            },
            {
                'page': 'home',
                'content_type': 'home_volunteer_section',
                'title': 'Volunteer Call-to-Action',
                'heading': 'Join Our Mission',
                'content': '<p>Be part of the change you want to see. Volunteer with Live Great Foundation and help us create lasting impact in communities across Kenya. Together, we can build a better future.</p>',
                'display_order': 6,
            },
            
            # About Page Content
            {
                'page': 'about',
                'content_type': 'about_main_content',
                'title': 'Main About Content',
                'heading': 'About Live Great Foundation',
                'content': '<p>Founded with a vision to create lasting positive change, Live Great Foundation works directly with communities across Kenya to address critical needs in education, health, environmental conservation, and economic development.</p><p>Our approach is community-centered, ensuring that local voices guide our programs and initiatives. We believe in empowering communities to become self-sufficient and resilient.</p>',
                'display_order': 1,
            },
            {
                'page': 'about',
                'content_type': 'about_history',
                'title': 'Our History',
                'heading': 'Our Journey',
                'content': '<p>Live Great Foundation was established to address the growing need for sustainable development programs in Kenya. Since our inception, we have worked with numerous communities, implementing programs that have positively impacted thousands of lives.</p>',
                'display_order': 2,
            },
            {
                'page': 'about',
                'content_type': 'about_values',
                'title': 'Our Values',
                'heading': 'What We Stand For',
                'content': '<ul><li><strong>Community-Centered:</strong> We put communities at the heart of everything we do</li><li><strong>Sustainability:</strong> We focus on long-term solutions that create lasting impact</li><li><strong>Transparency:</strong> We operate with openness and accountability</li><li><strong>Collaboration:</strong> We work in partnership with local communities and organizations</li></ul>',
                'display_order': 3,
            },
            
            # Programs Page Content
            {
                'page': 'programs',
                'content_type': 'programs_overview',
                'title': 'Programs Overview',
                'heading': 'Our Programs',
                'content': '<p>Live Great Foundation implements comprehensive programs designed to address the most pressing needs in Kenyan communities. Our programs are developed in partnership with local communities to ensure they are relevant, sustainable, and impactful.</p>',
                'display_order': 1,
            },
            {
                'page': 'programs',
                'content_type': 'programs_impact',
                'title': 'Impact Statistics',
                'heading': 'Our Impact',
                'content': '<p>Since our establishment, we have:</p><ul><li>Reached over 5,000 community members</li><li>Implemented 15+ community projects</li><li>Trained 200+ community health workers</li><li>Planted 10,000+ trees</li><li>Supported 500+ students with educational resources</li></ul>',
                'display_order': 2,
            },
            
            # Team Page Content
            {
                'page': 'team',
                'content_type': 'team_overview',
                'title': 'Team Overview',
                'heading': 'Meet Our Team',
                'content': '<p>Our dedicated team brings together diverse expertise in community development, public health, education, and environmental conservation. We are united by our commitment to creating positive change in Kenyan communities.</p>',
                'display_order': 1,
            },
            
            # Contact Page Content
            {
                'page': 'contact',
                'content_type': 'contact_main',
                'title': 'Main Contact Information',
                'heading': 'Get In Touch',
                'content': '<p>We would love to hear from you! Whether you are interested in partnering with us, volunteering, or learning more about our work, please don\'t hesitate to reach out.</p>',
                'display_order': 1,
            },
            {
                'page': 'contact',
                'content_type': 'contact_office',
                'title': 'Office Details',
                'heading': 'Visit Our Office',
                'content': '<p><strong>Address:</strong> Nairobi, Kenya</p><p><strong>Email:</strong> info@livegreatfoundation.org</p><p><strong>Phone:</strong> +254 700 000 000</p><p><strong>Office Hours:</strong> Monday - Friday, 8:00 AM - 5:00 PM</p>',
                'display_order': 2,
            },
            
            # Global Content
            {
                'page': 'home',
                'content_type': 'footer_content',
                'title': 'Footer Content',
                'heading': 'Live Great Foundation',
                'content': '<p>Empowering communities and transforming lives through sustainable development programs across Kenya.</p><p>© 2025 Live Great Foundation. All rights reserved.</p>',
                'display_order': 99,
            },
        ]

        created_count = 0
        updated_count = 0

        for data in content_data:
            content, created = WebsiteContent.objects.get_or_create(
                content_type=data['content_type'],
                defaults=data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created: {data["title"]}')
                )
            else:
                # Update existing content
                for key, value in data.items():
                    if key != 'content_type':
                        setattr(content, key, value)
                content.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'🔄 Updated: {data["title"]}')
                )

        self.stdout.write('')
        self.stdout.write('📊 Setup Summary:')
        self.stdout.write(f'   ✅ Created: {created_count} content items')
        self.stdout.write(f'   🔄 Updated: {updated_count} content items')
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ Website content setup completed!'))
        self.stdout.write('')
        self.stdout.write('📝 Next Steps:')
        self.stdout.write('   1. Visit admin panel to review and edit content')
        self.stdout.write('   2. Customize content for your specific needs')
        self.stdout.write('   3. Add images to enhance visual appeal')
        self.stdout.write('   4. Update templates to use new WebsiteContent model')


# Example usage:
"""
python manage.py setup_website_content
"""
