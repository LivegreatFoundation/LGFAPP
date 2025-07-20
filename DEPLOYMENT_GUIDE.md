# 🚀 Live Great Foundation - Render Deployment Guide
## Production-Ready Django Application Deployment

This guide provides step-by-step instructions for deploying the Live Great Foundation Django application to Render with all features working correctly.

---

## 📋 **Pre-Deployment Checklist**

### ✅ **Files Prepared**
- [x] **requirements.txt** - Updated with all dependencies
- [x] **build.sh** - Render build script (executable)
- [x] **render.yaml** - Infrastructure as Code configuration
- [x] **.env** - Production environment variables template
- [x] **blog/settings.py** - Updated for production with environment variables

### ✅ **Features Ready for Production**
- [x] **Excel Import System** - AI-assisted bulk blog post creation
- [x] **Email Notification System** - Professional branded notifications
- [x] **Admin Interface** - django-unfold with enhanced functionality
- [x] **Blog Categories & Tags** - 10 categories, 91 tags
- [x] **Database Integration** - Supabase PostgreSQL
- [x] **Security Settings** - HTTPS, HSTS, secure cookies

---

## 🔧 **Step 1: Render Account Setup**

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub account (recommended)
   - Connect your GitHub repository

2. **Repository Preparation**
   - Push all code to your GitHub repository
   - Ensure the main branch contains the latest code
   - Verify all deployment files are committed

---

## 🗄️ **Step 2: Database Configuration**

### **Option A: Use Existing Supabase Database**
1. **Verify Supabase Connection**
   - Ensure your Supabase project is active
   - Note the connection string format:
     ```
     postgresql://postgres.PROJECT_REF:PASSWORD@HOST:PORT/postgres
     ```

2. **Current Database Details**
   ```
   Host: aws-0-eu-central-1.pooler.supabase.com
   Port: 6543
   Database: postgres
   User: postgres.rhphjdabjfllajcwrbra
   Password: LGFweb2025!keke
   ```

### **Option B: Create New Render PostgreSQL Database**
1. In Render Dashboard → Create → PostgreSQL
2. Choose plan (Starter for testing, Standard+ for production)
3. Note the connection details for environment variables

---

## 🌐 **Step 3: Web Service Deployment**

### **Create Web Service**
1. **In Render Dashboard**
   - Click "Create" → "Web Service"
   - Connect your GitHub repository
   - Select the Live Great Foundation repository

2. **Basic Configuration**
   ```
   Name: live-great-foundation
   Region: Oregon (or your preferred region)
   Branch: main
   Runtime: Python 3
   Build Command: ./build.sh
   Start Command: gunicorn blog.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
   ```

3. **Plan Selection**
   - **Starter**: $7/month (for testing)
   - **Standard**: $25/month (recommended for production)
   - **Pro**: $85/month (for high traffic)

---

## 🔐 **Step 4: Environment Variables Configuration**

### **Required Environment Variables**
Set these in Render Dashboard → Your Service → Environment:

#### **Django Core**
```bash
SECRET_KEY=4+-Ts%frm&g^#Q&yFYtviZEap0rMi(+$JX&wnXL!dtoz1^RUBm
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,livegreatfoundation.org,www.livegreatfoundation.org
DJANGO_SETTINGS_MODULE=blog.settings
```

#### **Database**
```bash
DATABASE_URL=postgresql://postgres.rhphjdabjfllajcwrbra:LGFweb2025!keke@aws-0-eu-central-1.pooler.supabase.com:6543/postgres
```

#### **Email Configuration**
```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=dedeexpeditions@gmail.com
EMAIL_HOST_PASSWORD=roqu frlt wvof rqxk
DEFAULT_FROM_EMAIL=Live Great Foundation Technical Team <dedeexpeditions@gmail.com>
LGF_ADMIN_EMAIL=info@livegreatfoundation.org
```

#### **Security Settings**
```bash
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

#### **Site Configuration**
```bash
SITE_URL=https://your-app-name.onrender.com
SITE_NAME=Live Great Foundation
```

---

## 🚀 **Step 5: Deploy Application**

1. **Trigger Deployment**
   - Click "Create Web Service" or "Deploy Latest Commit"
   - Monitor build logs for any errors
   - Build process should complete in 3-5 minutes

2. **Build Process Verification**
   ```bash
   ✅ Installing dependencies
   ✅ Collecting static files
   ✅ Running migrations
   ✅ Creating superuser (if needed)
   ✅ Populating initial data
   ```

3. **Access Your Application**
   - URL: `https://your-app-name.onrender.com`
   - Admin: `https://your-app-name.onrender.com/admin/`

---

## 🔍 **Step 6: Post-Deployment Verification**

### **Test Core Functionality**
1. **Website Access**
   - [ ] Homepage loads correctly
   - [ ] Admin interface accessible
   - [ ] Login functionality works

2. **Excel Import System**
   - [ ] Navigate to `/admin/blogapp/post/`
   - [ ] Download template button works
   - [ ] Import functionality accessible
   - [ ] Sample import test successful

3. **Email Notifications**
   - [ ] Test email sending from admin
   - [ ] Verify SMTP connection
   - [ ] Check notification creation

4. **Database Operations**
   - [ ] Categories and tags visible
   - [ ] Blog posts can be created
   - [ ] Data persistence verified

---

## 🛠️ **Step 7: Custom Domain Setup (Optional)**

### **Configure Custom Domain**
1. **In Render Dashboard**
   - Go to your service → Settings → Custom Domains
   - Add `livegreatfoundation.org` and `www.livegreatfoundation.org`

2. **DNS Configuration**
   ```
   Type: CNAME
   Name: www
   Value: your-app-name.onrender.com
   
   Type: A
   Name: @
   Value: [Render IP provided in dashboard]
   ```

3. **Update Environment Variables**
   ```bash
   ALLOWED_HOSTS=livegreatfoundation.org,www.livegreatfoundation.org,your-app-name.onrender.com
   SITE_URL=https://livegreatfoundation.org
   ```

---

## 📊 **Step 8: Monitoring & Maintenance**

### **Health Monitoring**
- **Health Check URL**: `/admin/login/`
- **Logs**: Available in Render Dashboard
- **Metrics**: CPU, Memory, Response times

### **Regular Maintenance**
1. **Database Backups**
   - Supabase: Automatic backups enabled
   - Manual exports via admin interface

2. **Security Updates**
   - Monitor Django security releases
   - Update dependencies regularly
   - Review access logs

3. **Performance Monitoring**
   - Monitor response times
   - Check error rates
   - Scale resources as needed

---

## 🚨 **Troubleshooting Common Issues**

### **Build Failures**
```bash
# Check build logs for:
- Missing dependencies in requirements.txt
- Database connection issues
- Static file collection errors
- Migration failures
```

### **Runtime Errors**
```bash
# Common fixes:
- Verify environment variables
- Check database connectivity
- Confirm static files serving
- Review security settings
```

### **Email Issues**
```bash
# Verify:
- Gmail SMTP credentials
- App-specific password usage
- TLS/SSL settings
- Firewall restrictions
```

---

## 📞 **Support Resources**

### **Documentation**
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Django Deployment**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Supabase Docs**: [supabase.com/docs](https://supabase.com/docs)

### **Live Great Foundation Specific**
- **Admin Access**: `admin` / `LGFadmin2025!`
- **Email Support**: `info@livegreatfoundation.org`
- **Technical Contact**: Development team

---

## ✅ **Deployment Success Checklist**

- [ ] Application accessible at production URL
- [ ] Admin interface working with django-unfold theme
- [ ] Excel import system functional
- [ ] Email notifications sending correctly
- [ ] Database operations working
- [ ] Static files serving properly
- [ ] HTTPS enabled with security headers
- [ ] Custom domain configured (if applicable)
- [ ] Monitoring and logging active
- [ ] Backup strategy in place

---

*Deployment guide prepared for Live Great Foundation*  
*Django 5.0.9 + Render + Supabase + Production Security*  
*All features: Excel Import, Email Notifications, Admin Interface*
