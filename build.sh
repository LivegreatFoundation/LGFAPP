#!/usr/bin/env bash
# Live Great Foundation - Render Build Script
# This script runs during the build phase on Render

set -o errexit  # Exit on error

echo "🚀 Starting Live Great Foundation build process..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔧 Running Django management commands..."

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create superuser if it doesn't exist (optional, for initial deployment)
echo "👤 Creating superuser (if needed)..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'info@livegreatfoundation.org', 'LGFadmin2025!')
    print('✅ Superuser created: admin')
else:
    print('ℹ️  Superuser already exists')
" || echo "⚠️  Superuser creation skipped (may already exist)"

# Populate initial data if needed
echo "📊 Checking for initial blog data..."
python manage.py shell -c "
from blogapp.models import Category
from taggit.models import Tag
if Category.objects.count() == 0:
    print('📂 No categories found, running populate_blog_data...')
    import subprocess
    subprocess.run(['python', 'manage.py', 'populate_blog_data'], check=True)
    print('✅ Initial blog data populated')
else:
    print(f'ℹ️  Blog data already exists: {Category.objects.count()} categories, {Tag.objects.count()} tags')
" || echo "⚠️  Initial data population skipped"

echo "✅ Build process completed successfully!"
echo "🎉 Live Great Foundation is ready for deployment!"
