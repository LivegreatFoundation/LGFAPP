# Live Great Foundation Blog Categories and Tags

This document lists all the default categories and tags that have been created for the Live Great Foundation blog system.

## 📂 Blog Categories (10 total)

1. **Health & Wellness** - Articles about health, nutrition, and wellness programs
2. **Education** - Educational content and literacy programs  
3. **Community Development** - Community building and development initiatives
4. **Women Empowerment** - Programs and stories about empowering women and girls
5. **Environmental Sustainability** - Environmental conservation and sustainability efforts
6. **Youth Programs** - Programs and activities for young people
7. **Success Stories** - Inspiring stories from our community
8. **Events & News** - Foundation events, news, and announcements
9. **Partnerships** - Collaborations and partnership announcements
10. **Fundraising** - Fundraising campaigns and donation drives

## 🏷️ Blog Tags (88 total)

### Health & Wellness Tags
- nutrition, healthcare, mental-health, wellness, fitness
- maternal-health, child-health, hygiene, clean-water

### Education Tags  
- literacy, education, learning, skills-training, vocational-training
- adult-education, early-childhood, scholarships, books

### Community Tags
- community, development, empowerment, leadership, capacity-building
- social-impact, grassroots, local-initiatives, volunteer

### Women & Gender Tags
- women-empowerment, gender-equality, girls-education, women-leadership
- economic-empowerment, reproductive-health, gender-based-violence

### Environment Tags
- environment, sustainability, climate-change, conservation
- renewable-energy, waste-management, green-initiatives

### Youth Tags
- youth, children, mentorship, youth-leadership, sports
- arts, creativity, life-skills

### Program Tags
- training, workshop, seminar, conference, outreach
- awareness, campaign, advocacy, research

### Impact Tags
- success-story, testimonial, impact, transformation
- achievement, milestone, progress, results

### Partnership Tags
- partnership, collaboration, donor, sponsor, volunteer
- government, ngo, private-sector, international

### Location Tags (Kenya-specific)
- kenya, nairobi, rural, urban, africa, east-africa

### Foundation Specific Tags
- live-great-foundation, lgf, mission, vision, values
- annual-report, newsletter, update

## 🔧 Management Commands

### Populate Blog Data
```bash
python manage.py populate_blog_data
```

### Clear and Repopulate
```bash
python manage.py populate_blog_data --clear
```

## 📝 Usage Notes

- All categories have automatically generated slugs for URL-friendly navigation
- Tags are created with proper slugification for consistency
- Categories and tags can be managed through the Django admin interface
- The populate command is idempotent - running it multiple times won't create duplicates
- Use the `--clear` flag to reset all categories and tags before repopulating

## 🎯 Next Steps

1. **Access Admin Interface**: Visit `/admin/blogapp/category/` to manage categories
2. **View Tags**: Visit `/admin/taggit/tag/` to manage tags  
3. **Create Blog Posts**: Use these categories and tags when creating new blog posts
4. **Customize**: Add more categories or tags as needed through the admin interface

---

*Generated automatically by the Live Great Foundation blog management system*
