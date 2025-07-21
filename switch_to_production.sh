#!/bin/bash
# Switch to Production Environment

echo "🔄 Switching to Production Environment..."

# Copy production configuration
cp .env.production .env

echo "✅ Production environment activated!"
echo ""
echo "📋 Production Configuration:"
echo "   - Environment: PRODUCTION"
echo "   - Database: Supabase PostgreSQL"
echo "   - DEBUG=False"
echo "   - SECURE_SSL_REDIRECT=True"
echo "   - SESSION_COOKIE_SECURE=True"
echo "   - CSRF_COOKIE_SECURE=True"
echo "   - EMAIL_BACKEND=smtp"
echo "   - SITE_URL=https://your-app-name.onrender.com"
echo ""
echo "⚠️  IMPORTANT NOTES:"
echo "   - This configuration requires HTTPS!"
echo "   - Update ALLOWED_HOSTS with your actual domain"
echo "   - Update SITE_URL with your actual URL"
echo "   - Ensure Supabase database is accessible"
echo ""
echo "🚀 Ready for production deployment"
echo "📝 Remember to update environment variables in Render dashboard"
