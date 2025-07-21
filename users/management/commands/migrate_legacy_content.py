"""
Management command to migrate legacy Editpage content to the new WebsiteContent model
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from users.models import Editpage, WebsiteContent


class Command(BaseCommand):
    help = 'Migrate legacy Editpage content to the new WebsiteContent model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be migrated without actually doing it',
        )

    def handle(self, *args, **options):
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🔄 Migrating Legacy Content to New System'))
        self.stdout.write('=' * 70)

        # Mapping from old section_name to new content_type
        migration_mapping = {
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

        # Get page mapping from content_type
        page_mapping = {
            'home_hero_main': 'home',
            'home_hero_secondary': 'home',
            'home_hero_tertiary': 'home',
            'home_program_1': 'home',
            'home_program_2': 'home',
            'home_program_3': 'home',
            'home_about_preview': 'home',
            'home_mission_statement': 'home',
            'home_vision_statement': 'home',
            'home_volunteer_section': 'home',
            'footer_content': 'home',  # Global content
            'about_main_content': 'about',
            'programs_goddess_care': 'programs',
            'programs_reach': 'programs',
            'team_kelly': 'team',
            'team_elsie': 'team',
            'team_loise': 'team',
        }

        dry_run = options['dry_run']
        migrated_count = 0
        skipped_count = 0

        if dry_run:
            self.stdout.write(self.style.WARNING('🔍 DRY RUN MODE - No changes will be made'))
            self.stdout.write('')

        # Get all legacy content
        legacy_content = Editpage.objects.all()
        
        if not legacy_content.exists():
            self.stdout.write(self.style.WARNING('⚠️  No legacy content found to migrate'))
            return

        self.stdout.write(f'📊 Found {legacy_content.count()} legacy content items')
        self.stdout.write('')

        with transaction.atomic():
            for item in legacy_content:
                section_name = item.section_name
                
                if section_name not in migration_mapping:
                    self.stdout.write(
                        self.style.WARNING(f'⚠️  Skipping unknown section: {section_name}')
                    )
                    skipped_count += 1
                    continue

                new_content_type = migration_mapping[section_name]
                page = page_mapping[new_content_type]

                # Check if content already exists
                if WebsiteContent.objects.filter(content_type=new_content_type).exists():
                    self.stdout.write(
                        self.style.WARNING(f'⚠️  Content already exists for: {new_content_type}')
                    )
                    skipped_count += 1
                    continue

                if not dry_run:
                    # Create new WebsiteContent
                    new_content = WebsiteContent.objects.create(
                        page=page,
                        content_type=new_content_type,
                        title=f"Migrated: {item.get_section_name_display()}",
                        heading=item.heading,
                        content=item.content,
                        image=item.slider_image,
                        is_active=True,
                        display_order=migrated_count + 1,
                    )
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Migrated: {section_name} → {new_content_type}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'🔍 Would migrate: {section_name} → {new_content_type}')
                    )
                
                migrated_count += 1

        self.stdout.write('')
        self.stdout.write('📊 Migration Summary:')
        self.stdout.write(f'   ✅ Migrated: {migrated_count} items')
        self.stdout.write(f'   ⚠️  Skipped: {skipped_count} items')
        
        if dry_run:
            self.stdout.write('')
            self.stdout.write(self.style.WARNING('🔍 This was a dry run - no changes were made'))
            self.stdout.write('💡 Run without --dry-run to perform the actual migration')
        else:
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('✅ Migration completed successfully!'))
            self.stdout.write('')
            self.stdout.write('📝 Next Steps:')
            self.stdout.write('   1. Review migrated content in admin panel')
            self.stdout.write('   2. Update templates to use new WebsiteContent model')
            self.stdout.write('   3. Test website functionality')
            self.stdout.write('   4. Consider removing old Editpage model after verification')


# Example usage:
"""
# Dry run to see what would be migrated
python manage.py migrate_legacy_content --dry-run

# Actual migration
python manage.py migrate_legacy_content
"""
