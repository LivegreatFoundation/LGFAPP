#!/usr/bin/env python3
"""
Create Excel template for AI-assisted bulk blog post import
Live Great Foundation - Django Blog System
"""

import os
import sys
import django
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# Setup Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from blogapp.models import Category
from taggit.models import Tag

def create_blog_import_template():
    """Create comprehensive Excel template for blog post import"""
    
    # Create workbook and worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Blog Posts Import"
    
    # Define headers matching Django model fields
    headers = [
        'title',           # Required, max 1000 chars
        'content',         # Required, ProseEditor HTML content
        'Author',          # Required, max 1000 chars (note capital A)
        'category',        # Required, must match existing Category.title
        'status',          # Auto-filled as "published"
        'tags',            # Optional, comma-separated
        'featured',        # Optional, TRUE/FALSE
        'trending',        # Optional, TRUE/FALSE
        'image'            # Optional, leave blank for now
    ]
    
    # Header styling
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Add headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = border
    
    # Set column widths
    column_widths = {
        'A': 40,  # title
        'B': 60,  # content
        'C': 20,  # Author
        'D': 25,  # category
        'E': 15,  # status
        'F': 30,  # tags
        'G': 12,  # featured
        'H': 12,  # trending
        'I': 15   # image
    }
    
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width
    
    # Get existing categories and tags from database
    try:
        categories = [cat.title for cat in Category.objects.all().order_by('title')]
        tags = [tag.name for tag in Tag.objects.all().order_by('name')]
    except Exception as e:
        print(f"Warning: Could not fetch categories/tags from database: {e}")
        categories = ["Health & Wellness", "Education", "Community Development"]
        tags = ["health", "education", "community", "empowerment"]
    
    # Sample data for Live Great Foundation
    sample_data = [
        {
            'title': 'Empowering Women Through Digital Literacy in Rural Kenya',
            'content': '''<h2>Breaking Digital Barriers</h2>
<p>In the heart of rural Kenya, the Live Great Foundation is pioneering a transformative digital literacy program that's changing lives one click at a time. Our latest initiative has reached over 200 women in remote communities, providing them with essential computer skills and internet knowledge.</p>

<h3>Program Highlights</h3>
<ul>
<li>Basic computer operations and internet navigation</li>
<li>Online banking and mobile money management</li>
<li>Digital marketing for small businesses</li>
<li>Access to online educational resources</li>
</ul>

<p>The impact has been remarkable. Women who once felt disconnected from the digital world are now using technology to grow their businesses, access healthcare information, and connect with global markets.</p>

<blockquote>"This program has opened doors I never knew existed. I can now manage my shop's inventory online and reach customers beyond my village." - Mary Wanjiku, Program Participant</blockquote>

<p>As we continue to expand this program, we're committed to ensuring that digital literacy becomes a bridge to opportunity, not a barrier to progress.</p>''',
            'Author': 'Sarah Kimani',
            'category': 'Women Empowerment',
            'status': 'published',
            'tags': 'women-empowerment, digital-literacy, rural, kenya, education, technology',
            'featured': 'TRUE',
            'trending': 'FALSE',
            'image': ''
        },
        {
            'title': 'Clean Water Initiative Reaches 500 Households in Nairobi Slums',
            'content': '''<h2>Transforming Lives Through Clean Water Access</h2>
<p>Access to clean water is a fundamental human right, yet millions in urban slums lack this basic necessity. The Live Great Foundation's Clean Water Initiative has successfully installed water purification systems in 15 communities across Nairobi's informal settlements.</p>

<h3>Project Impact</h3>
<p>Over the past six months, our initiative has:</p>
<ul>
<li>Provided clean water access to 500+ households</li>
<li>Reduced waterborne diseases by 60% in target areas</li>
<li>Created 25 local jobs for system maintenance</li>
<li>Established 5 community water committees</li>
</ul>

<h3>Community Ownership</h3>
<p>What makes this project special is the emphasis on community ownership. Local residents are trained to maintain the systems, ensuring sustainability and creating a sense of pride and responsibility.</p>

<p>The ripple effects extend beyond health improvements. Children, especially girls, can now attend school regularly instead of spending hours fetching water. Women have more time for income-generating activities.</p>

<p><strong>Looking ahead:</strong> We plan to expand this initiative to reach 2,000 more households by the end of 2025.</p>''',
            'Author': 'Dr. James Mwangi',
            'category': 'Health & Wellness',
            'status': 'published',
            'tags': 'clean-water, health, nairobi, slums, community-development, sustainability',
            'featured': 'FALSE',
            'trending': 'TRUE',
            'image': ''
        },
        {
            'title': 'Youth Leadership Summit 2025: Shaping Tomorrow\'s Leaders',
            'content': '''<h2>Investing in the Next Generation</h2>
<p>The annual Live Great Foundation Youth Leadership Summit brought together 150 young leaders from across East Africa for three days of intensive training, networking, and inspiration.</p>

<h3>Summit Highlights</h3>
<p>This year's summit focused on:</p>
<ul>
<li><strong>Leadership Skills:</strong> Communication, decision-making, and team building</li>
<li><strong>Social Entrepreneurship:</strong> Creating businesses that solve social problems</li>
<li><strong>Digital Innovation:</strong> Leveraging technology for social impact</li>
<li><strong>Environmental Stewardship:</strong> Leading climate action in communities</li>
</ul>

<h3>Keynote Speakers</h3>
<p>Participants heard from inspiring leaders including:</p>
<ul>
<li>Hon. Grace Wanjiru - Cabinet Secretary for Youth Affairs</li>
<li>Dr. Peter Ndegwa - CEO, Safaricom</li>
<li>Wanjira Mathai - Environmental activist</li>
</ul>

<h3>Action Plans</h3>
<p>Each participant left with a concrete action plan to implement in their communities. Follow-up mentorship sessions will be conducted quarterly to support their initiatives.</p>

<blockquote>"The summit didn't just teach us about leadership - it showed us that we already have the power to create change in our communities." - Kevin Ochieng, Summit Participant</blockquote>''',
            'Author': 'Lucy Akinyi',
            'category': 'Youth Programs',
            'status': 'published',
            'tags': 'youth, leadership, summit, mentorship, entrepreneurship, east-africa',
            'featured': 'TRUE',
            'trending': 'TRUE',
            'image': ''
        }
    ]
    
    # Add sample data
    for row, data in enumerate(sample_data, 2):
        ws.cell(row=row, column=1, value=data['title'])
        ws.cell(row=row, column=2, value=data['content'])
        ws.cell(row=row, column=3, value=data['Author'])
        ws.cell(row=row, column=4, value=data['category'])
        ws.cell(row=row, column=5, value=data['status'])
        ws.cell(row=row, column=6, value=data['tags'])
        ws.cell(row=row, column=7, value=data['featured'])
        ws.cell(row=row, column=8, value=data['trending'])
        ws.cell(row=row, column=9, value=data['image'])
        
        # Set row height for content readability
        ws.row_dimensions[row].height = 60
    
    # Add data validation
    # Status dropdown
    status_validation = DataValidation(
        type="list",
        formula1='"draft,in_review,published"',
        allow_blank=False
    )
    status_validation.error = "Please select a valid status"
    status_validation.errorTitle = "Invalid Status"
    ws.add_data_validation(status_validation)
    status_validation.add(f"E2:E1000")
    
    # Featured/Trending validation
    bool_validation = DataValidation(
        type="list", 
        formula1='"TRUE,FALSE"',
        allow_blank=True
    )
    bool_validation.error = "Please enter TRUE or FALSE"
    bool_validation.errorTitle = "Invalid Boolean Value"
    ws.add_data_validation(bool_validation)
    bool_validation.add(f"G2:G1000")
    bool_validation.add(f"H2:H1000")
    
    # Category validation (if we have categories)
    if categories:
        category_list = ','.join(f'"{cat}"' for cat in categories)
        category_validation = DataValidation(
            type="list",
            formula1=category_list,
            allow_blank=False
        )
        category_validation.error = "Please select a valid category"
        category_validation.errorTitle = "Invalid Category"
        ws.add_data_validation(category_validation)
        category_validation.add(f"D2:D1000")
    
    return wb

if __name__ == "__main__":
    print("Creating blog import template...")
    wb = create_blog_import_template()
    
    # Create static directory if it doesn't exist
    static_dir = "static/admin/templates"
    os.makedirs(static_dir, exist_ok=True)
    
    # Save template
    template_path = f"{static_dir}/blog_post_import_template.xlsx"
    wb.save(template_path)
    
    print(f"✅ Template created successfully: {template_path}")
    print("📊 Template includes:")
    print("  • 9 columns matching Django Post model")
    print("  • 3 sample blog posts with realistic content")
    print("  • Data validation for status, featured, trending fields")
    print("  • Category dropdown with existing categories")
    print("  • Proper formatting and styling")
    print("  • Ready for AI-generated content import")
