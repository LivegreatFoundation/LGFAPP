from django.urls import path
from blogapp import views
from . import views


app_name = 'users'

urlpatterns = [
    # Legacy URLs (for backward compatibility)
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('programs/', views.programs, name='programs'),
    path('ourteam/', views.ourteam, name='ourteam'),
    path('contactus/', views.contactus, name='contactus'),
    path('ebooks/', views.ebooks, name='ebooks'),

    # Enhanced CMS URLs
    path('enhanced/', views.home, name='enhanced_home'),  # Use same home view for now
    path('enhanced/about/', views.enhanced_about, name='enhanced_about'),
    path('enhanced/programs/', views.enhanced_programs, name='enhanced_programs'),
    path('enhanced/team/', views.enhanced_team, name='enhanced_team'),
    path('enhanced/contact/', views.enhanced_contact, name='enhanced_contact'),
    path('program/<slug:slug>/', views.program_detail, name='program_detail'),
    path('search/', views.search_content, name='search_content'),
]

