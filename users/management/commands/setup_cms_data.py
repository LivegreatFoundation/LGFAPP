"""
Management command to set up initial CMS data for Live Great Foundation
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from users.models import PageSection, ContentBlock, TeamMember, Program, SiteSettings


class Command(BaseCommand):
    help = 'Set up initial CMS data for Live Great Foundation'

    def handle(self, *args, **options):
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🚀 Setting up Live Great Foundation CMS Data'))
        self.stdout.write('=' * 70)

        # Create Site Settings
        self.create_site_settings()
        
        # Create Page Sections
        self.create_page_sections()
        
        # Create Sample Team Members
        self.create_team_members()
        
        # Create Sample Programs
        self.create_programs()

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ CMS Data setup completed successfully!'))
        self.stdout.write('')

    def create_site_settings(self):
        """Create initial site settings"""
        self.stdout.write('📝 Creating site settings...')
        
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_name': 'Live Great Foundation',
                'tagline': 'Empowering Communities • Transforming Lives',
                'email': 'info@livegreatfoundation.org',
                'phone': '+254 700 000 000',
                'address': 'Nairobi, Kenya',
                'meta_description': 'Live Great Foundation is a nonprofit organization dedicated to empowering communities and transforming lives through sustainable development programs in Kenya.',
                'meta_keywords': 'nonprofit, foundation, community development, Kenya, empowerment, education, health, environment',
                'footer_text': '<p>Live Great Foundation is committed to creating lasting positive change in communities across Kenya through innovative programs and partnerships.</p>',
                'copyright_text': '© 2025 Live Great Foundation. All rights reserved.',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('  ✅ Site settings created'))
        else:
            self.stdout.write(self.style.WARNING('  ⚠️  Site settings already exist'))

    def create_page_sections(self):
        """Create initial page sections"""
        self.stdout.write('📄 Creating page sections...')
        
        sections_data = [
            {
                'title': 'Hero Section',
                'page': 'home',
                'section_type': 'hero',
                'slug': 'home-hero',
                'heading': 'Empowering Communities, Transforming Lives',
                'subheading': 'Join us in creating sustainable change across Kenya through education, health, and environmental programs.',
                'content': '<p>At Live Great Foundation, we believe every community has the potential for greatness. Through our comprehensive programs and partnerships, we work hand-in-hand with local communities to create lasting positive change.</p>',
                'order': 1,
            },
            {
                'title': 'About Us Section',
                'page': 'home',
                'section_type': 'about',
                'slug': 'home-about',
                'heading': 'Our Mission',
                'subheading': 'Building stronger communities through sustainable development',
                'content': '<p>Live Great Foundation is dedicated to empowering communities across Kenya through innovative programs that address education, health, environmental sustainability, and economic empowerment. We work directly with local communities to identify needs and develop solutions that create lasting impact.</p>',
                'order': 2,
            },
            {
                'title': 'Mission Statement',
                'page': 'about',
                'section_type': 'mission',
                'slug': 'about-mission',
                'heading': 'Our Mission',
                'content': '<p>To empower communities across Kenya by providing access to quality education, healthcare, environmental conservation programs, and economic opportunities that create sustainable positive change.</p>',
                'order': 1,
            },
            {
                'title': 'Vision Statement',
                'page': 'about',
                'section_type': 'vision',
                'slug': 'about-vision',
                'heading': 'Our Vision',
                'content': '<p>A Kenya where every community thrives with access to quality education, healthcare, clean environment, and economic opportunities for all.</p>',
                'order': 2,
            },
        ]
        
        created_count = 0
        for section_data in sections_data:
            section, created = PageSection.objects.get_or_create(
                slug=section_data['slug'],
                defaults=section_data
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'  ✅ Created {created_count} page sections'))

    def create_team_members(self):
        """Create sample team members"""
        self.stdout.write('👥 Creating team members...')
        
        team_data = [
            {
                'name': 'Kelly Wanjiku',
                'position': 'Executive Director',
                'bio': '<p>Kelly brings over 15 years of experience in nonprofit management and community development. She holds a Master\'s degree in Development Studies and is passionate about creating sustainable change in rural communities.</p>',
                'email': 'kelly@livegreatfoundation.org',
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Elsie Muthoni',
                'position': 'Program Manager',
                'bio': '<p>Elsie oversees our education and health programs across Kenya. With a background in public health and education, she ensures our programs meet the highest standards and create meaningful impact.</p>',
                'email': 'elsie@livegreatfoundation.org',
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Loise Njeri',
                'position': 'Community Outreach Coordinator',
                'bio': '<p>Loise works directly with communities to identify needs and implement programs. Her deep understanding of local cultures and languages makes her an invaluable bridge between the foundation and the communities we serve.</p>',
                'email': 'loise@livegreatfoundation.org',
                'is_featured': True,
                'order': 3,
            },
        ]
        
        created_count = 0
        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'  ✅ Created {created_count} team members'))

    def create_programs(self):
        """Create sample programs"""
        self.stdout.write('📋 Creating programs...')
        
        programs_data = [
            {
                'name': 'Education Empowerment Initiative',
                'slug': 'education-empowerment',
                'short_description': 'Providing quality education and learning resources to underserved communities across Kenya.',
                'full_description': '<p>Our Education Empowerment Initiative focuses on improving access to quality education in rural and underserved communities. We build schools, train teachers, provide learning materials, and support students with scholarships.</p><p>Through partnerships with local communities and government agencies, we have established learning centers that serve over 2,000 students annually.</p>',
                'objectives': '<ul><li>Build and renovate schools in underserved areas</li><li>Train and support local teachers</li><li>Provide learning materials and technology</li><li>Offer scholarships to deserving students</li></ul>',
                'target_audience': 'Children and youth in rural communities',
                'location': 'Rural Kenya',
                'beneficiaries_count': 2000,
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Community Health Program',
                'slug': 'community-health',
                'short_description': 'Improving healthcare access and health outcomes in rural communities through mobile clinics and health education.',
                'full_description': '<p>Our Community Health Program brings essential healthcare services directly to communities that lack access to medical facilities. We operate mobile clinics, train community health workers, and provide health education.</p><p>The program focuses on preventive care, maternal health, child nutrition, and treatment of common diseases.</p>',
                'objectives': '<ul><li>Operate mobile health clinics</li><li>Train community health workers</li><li>Provide health education and awareness</li><li>Support maternal and child health</li></ul>',
                'target_audience': 'Rural communities with limited healthcare access',
                'location': 'Remote areas of Kenya',
                'beneficiaries_count': 1500,
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Environmental Conservation Initiative',
                'slug': 'environmental-conservation',
                'short_description': 'Promoting environmental sustainability through tree planting, clean energy, and conservation education.',
                'full_description': '<p>Our Environmental Conservation Initiative addresses climate change and environmental degradation through community-based conservation programs. We focus on reforestation, clean energy solutions, and environmental education.</p><p>Working with local communities, we have planted over 10,000 trees and established community gardens that provide both food security and environmental benefits.</p>',
                'objectives': '<ul><li>Plant trees and restore degraded lands</li><li>Promote clean energy solutions</li><li>Provide environmental education</li><li>Support sustainable agriculture practices</li></ul>',
                'target_audience': 'Rural communities and environmental groups',
                'location': 'Various regions across Kenya',
                'beneficiaries_count': 800,
                'is_featured': True,
                'order': 3,
            },
        ]
        
        created_count = 0
        for program_data in programs_data:
            program, created = Program.objects.get_or_create(
                slug=program_data['slug'],
                defaults=program_data
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'  ✅ Created {created_count} programs'))


# Example usage:
"""
python manage.py setup_cms_data
"""
