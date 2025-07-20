# 🚀 AI-Assisted Blog Import Guide
## Live Great Foundation - Django Blog System

This guide provides a complete workflow for using AI tools to generate blog content in bulk and importing it efficiently into the Live Great Foundation website.

## 📋 Quick Start Workflow

1. **Download Template** → 2. **Generate AI Content** → 3. **Fill Template** → 4. **Import to Website**

---

## 📥 Step 1: Download the Import Template

### From Django Admin:
1. Navigate to **Admin Panel** → **Blog Posts** 
2. Click the **"📥 Download Import Template"** button
3. Save `blog_post_import_template.xlsx` to your computer

### Template Structure:
The template includes 9 columns matching the Django Post model:

| Column | Required | Description | Example |
|--------|----------|-------------|---------|
| `title` | ✅ Yes | Post title (max 1000 chars) | "Empowering Women Through Digital Literacy" |
| `content` | ✅ Yes | HTML content for ProseEditor | `<h2>Introduction</h2><p>Content...</p>` |
| `Author` | ✅ Yes | Author name (max 1000 chars) | "Sarah Kimani" |
| `category` | ✅ Yes | Must match existing category exactly | "Women Empowerment" |
| `status` | ✅ Yes | Post status (defaults to "published") | "published" |
| `tags` | ❌ No | Comma-separated tag list | "women, education, kenya" |
| `featured` | ❌ No | TRUE/FALSE (defaults to FALSE) | "TRUE" |
| `trending` | ❌ No | TRUE/FALSE (defaults to FALSE) | "FALSE" |
| `image` | ❌ No | Leave blank for now | "" |

---

## 🤖 Step 2: AI Content Generation

### Recommended AI Tools:
- **ChatGPT** (GPT-4 or GPT-3.5)
- **Claude** (Anthropic)
- **Gemini** (Google)
- **Perplexity AI**

### Optimal AI Prompts:

#### For Blog Post Generation:
```
Create [NUMBER] blog posts for the Live Great Foundation, a non-profit organization in Kenya focused on community development, women empowerment, education, health, and environmental sustainability.

For each blog post, provide:
1. Title (engaging, 50-80 characters)
2. HTML content (500-800 words) with proper headings, paragraphs, lists, and quotes
3. Author name (realistic Kenyan name)
4. Category (choose from: Health & Wellness, Education, Community Development, Women Empowerment, Environmental Sustainability, Youth Programs, Success Stories, Events & News, Partnerships, Fundraising)
5. Tags (3-6 relevant tags, comma-separated)

Content should be:
- Inspiring and positive
- Focused on real impact and community stories
- Include specific examples and outcomes
- Use proper HTML formatting (<h2>, <h3>, <p>, <ul>, <li>, <blockquote>)
- Authentic to African/Kenyan context

Format the output as a table or structured list that I can easily copy into Excel.
```

#### For Specific Topics:
```
Generate 5 blog posts about [SPECIFIC TOPIC] for Live Great Foundation in Kenya. Each post should:
- Focus on real community impact
- Include success stories or testimonials
- Use HTML formatting for web display
- Be 500-800 words
- Include relevant statistics or outcomes
- Match the organization's mission of empowerment and development

Topics to cover: [LIST SPECIFIC SUBTOPICS]
```

---

## 📝 Step 3: Fill the Excel Template

### Content Formatting Guidelines:

#### HTML Content Best Practices:
```html
<!-- Use proper heading hierarchy -->
<h2>Main Section Title</h2>
<h3>Subsection Title</h3>

<!-- Structure paragraphs clearly -->
<p>Your paragraph content here. Keep paragraphs focused and readable.</p>

<!-- Use lists for better readability -->
<ul>
<li>First point</li>
<li>Second point</li>
<li>Third point</li>
</ul>

<!-- Add impactful quotes -->
<blockquote>"This program changed my life completely." - Community Member</blockquote>

<!-- Emphasize key points -->
<p><strong>Important:</strong> Key information here.</p>
<p><em>Note:</em> Additional context here.</p>
```

#### Category Reference:
- **Health & Wellness**: Health programs, nutrition, clean water, medical initiatives
- **Education**: Literacy programs, schools, training, scholarships
- **Community Development**: Infrastructure, capacity building, local initiatives
- **Women Empowerment**: Women's programs, gender equality, economic empowerment
- **Environmental Sustainability**: Conservation, climate action, green initiatives
- **Youth Programs**: Youth leadership, mentorship, sports, arts
- **Success Stories**: Testimonials, achievements, transformations
- **Events & News**: Foundation events, announcements, updates
- **Partnerships**: Collaborations, donor relations, alliances
- **Fundraising**: Campaigns, donation drives, financial appeals

#### Tag Examples by Category:
- **Health**: `health, nutrition, clean-water, maternal-health, hygiene`
- **Education**: `education, literacy, training, scholarships, learning`
- **Community**: `community, development, empowerment, grassroots, local-initiatives`
- **Women**: `women-empowerment, gender-equality, economic-empowerment`
- **Environment**: `environment, sustainability, climate-change, conservation`
- **Youth**: `youth, mentorship, leadership, sports, creativity`

### Data Validation Features:
- **Status Dropdown**: Automatically limits to "draft", "in_review", "published"
- **Boolean Fields**: TRUE/FALSE dropdowns for featured/trending
- **Category Dropdown**: Shows all existing categories
- **Required Field Highlighting**: Visual indicators for mandatory fields

---

## 📤 Step 4: Import Process

### Import Steps:
1. **Access Import**: In Django Admin → Blog Posts → **Import** button (top-right)
2. **Upload File**: Select your filled Excel template
3. **Preview Import**: Review the preview to check for errors
4. **Confirm Import**: Click "Confirm import" to add posts to the website
5. **Verify Results**: Check the import summary and any error messages

### Import Features:
- **Automatic Defaults**: Status defaults to "published", booleans default to FALSE
- **Tag Creation**: New tags are automatically created if they don't exist
- **Duplicate Prevention**: Uses title as unique identifier to prevent duplicates
- **Error Reporting**: Clear messages for any formatting or validation issues
- **Batch Processing**: Efficiently handles 50+ posts in a single import

### Common Import Issues & Solutions:

| Issue | Cause | Solution |
|-------|-------|----------|
| "Category not found" | Typo in category name | Use exact category names from dropdown |
| "Invalid HTML" | Malformed HTML tags | Check HTML syntax, ensure tags are closed |
| "Title too long" | Title exceeds 1000 characters | Shorten title to under 1000 characters |
| "Missing required field" | Empty title, content, or Author | Fill all required fields |
| "Invalid boolean value" | Wrong TRUE/FALSE format | Use exactly "TRUE" or "FALSE" |

---

## 🎯 Best Practices

### Content Quality:
- **Authentic Voice**: Ensure AI content matches Live Great Foundation's tone
- **Local Context**: Include Kenyan/African cultural references and context
- **Impact Focus**: Emphasize real outcomes and community benefits
- **Visual Structure**: Use headings, lists, and quotes for readability

### Batch Processing:
- **Recommended Batch Size**: 20-50 posts per import for optimal performance
- **Test First**: Import 2-3 posts first to verify formatting
- **Review Content**: Always review AI-generated content before importing
- **Backup Strategy**: Keep Excel files as backup of imported content

### SEO Optimization:
- **Title Length**: Keep titles 50-80 characters for optimal SEO
- **Content Length**: Aim for 500-800 words per post
- **Tag Strategy**: Use 3-6 relevant tags per post
- **Category Consistency**: Maintain consistent categorization

---

## 🔧 Technical Notes

### ProseEditor Compatibility:
- Supports standard HTML tags: `<h1>-<h6>`, `<p>`, `<ul>`, `<ol>`, `<li>`, `<blockquote>`, `<strong>`, `<em>`
- Automatically handles line breaks and formatting
- Preserves HTML structure during import

### Database Integration:
- Uses Supabase PostgreSQL backend
- Automatic slug generation for categories and tags
- Full-text search indexing for imported content
- Optimized for django-unfold admin interface

### Performance Considerations:
- Connection pooling optimized for bulk imports
- Efficient tag creation and association
- Minimal database queries during import process
- Progress tracking for large imports

---

## 📞 Support

For technical issues or questions:
- **Admin Interface**: Use the Django admin help system
- **Import Errors**: Check the import summary for specific error messages
- **Content Guidelines**: Refer to Live Great Foundation content standards
- **Technical Support**: Contact the development team

---

*Last updated: January 2025 | Live Great Foundation Blog System v2.0*
