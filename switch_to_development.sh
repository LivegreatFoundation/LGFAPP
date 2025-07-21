#!/bin/bash
# Switch to Development Environment

echo "🔄 Switching to Development Environment..."

# Copy development configuration
cp .env.development .env

echo "✅ Development environment activated!"
echo ""
echo "📋 Development Configuration:"
echo "   - Environment: DEVELOPMENT"
echo "   - Database: SQLite (db.sqlite3)"
echo "   - DEBUG=True"
echo "   - SECURE_SSL_REDIRECT=False"
echo "   - SESSION_COOKIE_SECURE=False"
echo "   - CSRF_COOKIE_SECURE=False"
echo "   - EMAIL_BACKEND=console"
echo "   - SITE_URL=http://localhost:8000"
echo "   - ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0"
echo ""
echo "🗄️  Database Setup:"
echo "   Run: python manage.py migrate"
echo "   Run: python manage.py setup_cms_data"
echo ""
echo "🚀 Start Server:"
echo "   Run: python manage.py runserver"
echo ""
echo "🌐 Access URLs:"
echo "   - http://localhost:8000"
echo "   - http://127.0.0.1:8000"
echo "   - http://0.0.0.0:8000"
echo ""
echo "🔧 Admin Panel:"
echo "   - http://localhost:8000/admin/"
echo "   - Username: admin"
echo "   - Password: LGFadmin2025!"
