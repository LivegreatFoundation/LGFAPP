# 📝 Live Great Foundation - Content Management System User Guide
## Complete Guide for Non-Technical Users

This guide provides step-by-step instructions for managing website content through the enhanced admin interface.

---

## 🚀 **Getting Started**

### **Accessing the Admin Interface**
1. **Navigate to**: `https://your-website.com/admin/`
2. **Login with your credentials**:
   - Username: `admin`
   - Password: `LGFadmin2025!`
3. **You'll see the enhanced admin dashboard** with django-unfold theme

### **Admin Dashboard Overview**
The admin interface is organized into sections:
- **📄 Page Sections**: Manage different sections of your website pages
- **🧩 Content Blocks**: Individual content pieces within sections
- **👥 Team Members**: Manage team member profiles
- **📋 Programs**: Manage foundation programs
- **⚙️ Site Settings**: Global website settings

---

## 📄 **Managing Page Sections**

### **What are Page Sections?**
Page sections are the main building blocks of your website pages. Each section can contain:
- Heading and subheading
- Rich text content
- Background and featured images
- Multiple content blocks

### **Creating a New Page Section**
1. **Go to**: Admin Dashboard → Page Sections → Add Page Section
2. **Fill in the basic information**:
   - **Title**: Internal name for admin reference (e.g., "Home Hero Section")
   - **Page**: Select which page this section belongs to
   - **Section Type**: Choose the type of section (Hero, About, Mission, etc.)
   - **Slug**: Unique identifier (auto-generated from title)

3. **Add content**:
   - **Heading**: Main title visible on the website
   - **Subheading**: Subtitle or tagline
   - **Content**: Use the rich text editor for detailed content

4. **Upload images** (optional):
   - **Background Image**: Will appear behind the section content
   - **Featured Image**: Will appear within the section content

5. **Set display options**:
   - **Is Active**: Check to show on website
   - **Order**: Number determining display order (lower numbers appear first)
   - **CSS Classes**: Advanced styling options (leave blank if unsure)

6. **Click "Save"** to create the section

### **Editing Existing Sections**
1. **Go to**: Admin Dashboard → Page Sections
2. **Find the section** you want to edit
3. **Click on the section title** to open the edit form
4. **Make your changes** and click "Save"
5. **Use the "Preview" button** to see changes on the website

---

## 🧩 **Managing Content Blocks**

### **What are Content Blocks?**
Content blocks are individual pieces of content within a page section. Types include:
- **Text Block**: Rich text content
- **Image Block**: Images with captions
- **Video Block**: Embedded videos
- **Quote Block**: Highlighted quotes
- **Statistics Block**: Number displays
- **Call to Action Block**: Buttons and action prompts
- **Gallery Block**: Image galleries

### **Adding Content Blocks to a Section**
1. **Edit a Page Section** (see above)
2. **Scroll down to "Content Blocks"** section
3. **Click "Add another Content Block"**
4. **Fill in the block details**:
   - **Title**: Internal reference name
   - **Block Type**: Choose from dropdown
   - **Order**: Display order within the section
   - **Content**: Add text, images, or other media based on block type

5. **Save the section** to apply changes

### **Content Block Types Guide**

#### **Text Block**
- Use for paragraphs, lists, and formatted text
- Rich text editor supports bold, italic, links, lists
- Perfect for main content areas

#### **Image Block**
- Upload images with optional captions
- Images are automatically optimized for web
- Use for showcasing photos, infographics, etc.

#### **Quote Block**
- Highlight important quotes or testimonials
- Include author attribution
- Automatically styled with special formatting

#### **Statistics Block**
- Display important numbers (e.g., "2000+ Beneficiaries")
- Include both number and descriptive label
- Eye-catching display for impact metrics

#### **Call to Action Block**
- Create buttons that encourage user action
- Include button text and destination URL
- Use for "Donate Now", "Learn More", etc.

---

## 👥 **Managing Team Members**

### **Adding a New Team Member**
1. **Go to**: Admin Dashboard → Team Members → Add Team Member
2. **Fill in basic information**:
   - **Name**: Full name
   - **Position**: Job title or role
   - **Bio**: Use rich text editor for biography

3. **Add contact information**:
   - **Email**: Professional email address
   - **Phone**: Contact number
   - **LinkedIn URL**: Professional profile link
   - **Twitter URL**: Social media profile

4. **Upload photo**:
   - Use high-quality professional headshot
   - Recommended size: 400x400 pixels minimum

5. **Set display options**:
   - **Is Featured**: Show on homepage
   - **Is Active**: Show on team page
   - **Order**: Display order

### **Managing Team Display**
- **Featured team members** appear on the homepage
- **All active team members** appear on the team page
- **Order numbers** control the sequence of display
- **Inactive members** are hidden but not deleted

---

## 📋 **Managing Programs**

### **Creating a New Program**
1. **Go to**: Admin Dashboard → Programs → Add Program
2. **Basic information**:
   - **Name**: Program title
   - **Slug**: URL-friendly name (auto-generated)
   - **Short Description**: Brief summary for cards and previews
   - **Full Description**: Detailed description with rich text

3. **Program details**:
   - **Objectives**: Program goals and objectives
   - **Target Audience**: Who the program serves
   - **Location**: Where the program operates
   - **Beneficiaries Count**: Number of people helped
   - **Start Date**: When the program began

4. **Upload images**:
   - **Featured Image**: Main program image
   - **Gallery Images**: Additional photos (add via inline forms)

5. **Display settings**:
   - **Is Featured**: Show on homepage
   - **Is Active**: Show on programs page
   - **Order**: Display sequence

### **Adding Program Gallery Images**
1. **While editing a program**, scroll to "Program Images" section
2. **Click "Add another Program Image"**
3. **Upload image** and add caption
4. **Set order** for display sequence
5. **Save the program**

---

## ⚙️ **Site Settings**

### **Managing Global Settings**
1. **Go to**: Admin Dashboard → Site Settings
2. **Edit the single settings record** (only one exists)

### **Site Identity**
- **Site Name**: Your organization name
- **Tagline**: Motto or brief description
- **Logo**: Upload organization logo
- **Favicon**: Small icon for browser tabs

### **Contact Information**
- **Email**: Main contact email
- **Phone**: Primary phone number
- **Address**: Physical address

### **Social Media**
- Add URLs for all social media profiles
- Leave blank if not using a particular platform

### **SEO Settings**
- **Meta Description**: Default description for search engines
- **Meta Keywords**: Keywords for search optimization

### **Footer Content**
- **Footer Text**: Rich text content for website footer
- **Copyright Text**: Copyright notice

---

## 🎨 **Using the Rich Text Editor**

### **Editor Features**
The rich text editor (django-prose-editor) provides:
- **Bold, Italic, Underline**: Text formatting
- **Headings**: H1, H2, H3 for structure
- **Lists**: Bulleted and numbered lists
- **Links**: Add links to other pages or websites
- **Images**: Insert images directly into content
- **Quotes**: Blockquote formatting

### **Best Practices**
1. **Use headings** to structure content
2. **Keep paragraphs short** for better readability
3. **Add links** to relevant pages or external resources
4. **Use lists** to break up information
5. **Include images** to make content engaging

### **Image Guidelines**
- **File formats**: JPG, PNG, WebP
- **File size**: Keep under 2MB for faster loading
- **Dimensions**: Minimum 800px wide for featured images
- **Quality**: Use high-resolution images that look professional

---

## 📱 **Mobile Responsiveness**

### **Automatic Optimization**
- All content is automatically optimized for mobile devices
- Images resize automatically
- Text remains readable on all screen sizes
- Navigation adapts to mobile screens

### **Testing Your Changes**
1. **Make changes** in the admin
2. **View the website** on your computer
3. **Test on mobile** by resizing your browser window
4. **Check different pages** to ensure consistency

---

## 🔍 **Tips for Success**

### **Content Writing Tips**
1. **Write for your audience**: Use language your community understands
2. **Be specific**: Include concrete examples and numbers
3. **Tell stories**: Share real impact stories and testimonials
4. **Keep it current**: Update content regularly
5. **Use action words**: Encourage engagement and participation

### **Image Best Practices**
1. **Show real people**: Use authentic photos of your work
2. **High quality**: Invest in good photography
3. **Diverse representation**: Include diverse communities
4. **Consistent style**: Maintain visual consistency
5. **Optimize file sizes**: Compress images for faster loading

### **SEO Optimization**
1. **Use descriptive headings**: Help search engines understand content
2. **Include keywords naturally**: Don't force keyword stuffing
3. **Write meta descriptions**: Summarize page content
4. **Use alt text for images**: Describe images for accessibility
5. **Create internal links**: Link to other pages on your site

---

## 🆘 **Getting Help**

### **Common Issues**
- **Can't see changes**: Clear your browser cache and refresh
- **Images not uploading**: Check file size (must be under 2MB)
- **Rich text not saving**: Ensure you click "Save" after editing
- **Page not displaying**: Check that "Is Active" is checked

### **Support Resources**
- **Admin Help**: Look for help text under each field
- **Preview Function**: Use preview buttons to see changes
- **Backup**: Changes are automatically saved to database
- **Recovery**: Contact technical support if you need help

### **Contact Information**
- **Technical Support**: Contact your web developer
- **Training**: Request additional training sessions
- **Documentation**: Refer to this guide for step-by-step instructions

---

## 🎉 **Congratulations!**

You now have the tools to manage your website content effectively. Remember:
- **Start small**: Make one change at a time
- **Preview often**: Check your changes before publishing
- **Stay consistent**: Maintain your organization's voice and style
- **Update regularly**: Keep content fresh and current
- **Ask for help**: Don't hesitate to reach out when needed

Your website is now a powerful tool for sharing your organization's mission and impact with the world!

---

*Live Great Foundation Content Management System*  
*User Guide v1.0 - January 2025*
