from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q

# Import all models
from .models import (
    Editpage, SecondSection, SecondSectionIcon, SecondSectionBox,
    PageSection, ContentBlock, TeamMember, Program, ProgramImage, SiteSettings
)


def home(request):
    """
    Enhanced home view that uses both legacy and new content management systems
    """
    # Get site settings
    site_settings = SiteSettings.objects.first()

    # Get new page sections for home page
    home_sections = PageSection.objects.filter(
        page='home',
        is_active=True
    ).prefetch_related('content_blocks').order_by('order')

    # Get featured programs
    featured_programs = Program.objects.filter(
        is_featured=True,
        is_active=True
    ).order_by('order')[:3]

    # Get featured team members
    featured_team = TeamMember.objects.filter(
        is_featured=True,
        is_active=True
    ).order_by('order')[:3]

    # Legacy content (for backward compatibility)
    hnew = Editpage.objects.filter(section_name='hnew').first()
    hneww = Editpage.objects.filter(section_name='hneww').first()
    hnewww = Editpage.objects.filter(section_name='hnewww').first()
    Programme1 = Editpage.objects.filter(section_name='Programme1').first()
    Programme2 = Editpage.objects.filter(section_name='Programme2').first()
    Programme3 = Editpage.objects.filter(section_name='Programme3').first()
    about_us = Editpage.objects.filter(section_name='about_us').first()
    mission = Editpage.objects.filter(section_name='mission').first()
    vision = Editpage.objects.filter(section_name='vision').first()
    volunteer = Editpage.objects.filter(section_name='Volunteer').first()
    footer = Editpage.objects.filter(section_name='footer').first()
    team1 = Editpage.objects.filter(section_name='team1').first()
    team2 = Editpage.objects.filter(section_name='team2').first()
    team3 = Editpage.objects.filter(section_name='team3').first()
    home_section = Editpage.objects.filter(section_name='home_section').first()
    second_section = SecondSection.objects.first()
    second_section_icons = SecondSectionIcon.objects.all().order_by('order')
    second_section_box = SecondSectionBox.objects.first()

    # Enhanced context with both new and legacy content
    content = {
        # Site settings
        'site_settings': site_settings,

        # New content management system
        'home_sections': home_sections,
        'featured_programs': featured_programs,
        'featured_team': featured_team,

        # Legacy content (for backward compatibility)
        'Programme1': Programme1,
        'Programme2': Programme2,
        'Programme3': Programme3,
        'hnew': hnew,
        'hneww': hneww,
        'hnewww': hnewww,
        'about_us': about_us,
        'mission': mission,
        'vision': vision,
        'volunteer': volunteer,
        'footer': footer,
        'team1': team1,
        'team2': team2,
        'team3': team3,
        'second_section': second_section,
        'second_section_icons': second_section_icons,
        'second_section_box': second_section_box,


    }

    return render(request, 'index.html', content)

def aboutus(request):
    aboutUs = Editpage.objects.filter(section_name='aboutUs').first()
    footer = Editpage.objects.filter(section_name='footer').first()
    volunteer = Editpage.objects.filter(section_name='Volunteer').first()
    content = {
        'volunteer': volunteer,
        'footer': footer,
        'aboutUs': aboutUs,

    }

    return render(request, 'aboutus.html', content)

def programs(request):
    footer = Editpage.objects.filter(section_name='footer').first()
    our_programs = Editpage.objects.filter(section_name='our_Programs').first()
    reach = Editpage.objects.filter(section_name='reach').first()
    volunteer = Editpage.objects.filter(section_name='Volunteer').first()

    content = {
        'our_programs': our_programs,
        'footer': footer,
        'reach': reach,
        'volunteer': volunteer,

    }
    return render(request, 'programs.html', content)

def ourteam(request):
    volunteer = Editpage.objects.filter(section_name='Volunteer').first()
    footer = Editpage.objects.filter(section_name='footer').first()
    team1 = Editpage.objects.filter(section_name='team1').first()
    team2 = Editpage.objects.filter(section_name='team2').first()
    team3 = Editpage.objects.filter(section_name='team3').first()
    content = {

        'volunteer': volunteer,
        'footer': footer,
        'team1': team1,
        'team2': team2,
        'team3': team3,

    }

    return render(request, 'ourteam.html', content)

def contactus(request):

    return render(request, 'contactus.html')

def ebooks(request):
    footer = Editpage.objects.filter(section_name='footer').first()
    volunteer = Editpage.objects.filter(section_name='Volunteer').first()

    content = {
        'footer': footer,
        'volunteer': volunteer,
    }

    return render(request, 'ebooks.html', content)

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('.')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered!')
                return redirect('.')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return redirect('blog')
        else:
            messages.info(request, 'Password not matching!')
            return render('.')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('.')
    else:
        return render(request, 'login.html')


# ============================================================================
# ENHANCED CONTENT MANAGEMENT VIEWS
# ============================================================================

def enhanced_about(request):
    """Enhanced about page using new content management system"""
    site_settings = SiteSettings.objects.first()
    about_sections = PageSection.objects.filter(
        page='about',
        is_active=True
    ).prefetch_related('content_blocks').order_by('order')

    team_members = TeamMember.objects.filter(is_active=True).order_by('order')

    context = {
        'site_settings': site_settings,
        'about_sections': about_sections,
        'team_members': team_members,
    }

    return render(request, 'enhanced_about.html', context)


def enhanced_programs(request):
    """Enhanced programs page using new content management system"""
    site_settings = SiteSettings.objects.first()
    programs_sections = PageSection.objects.filter(
        page='programs',
        is_active=True
    ).prefetch_related('content_blocks').order_by('order')

    programs = Program.objects.filter(is_active=True).order_by('order')

    context = {
        'site_settings': site_settings,
        'programs_sections': programs_sections,
        'programs': programs,
    }

    return render(request, 'enhanced_programs.html', context)


def program_detail(request, slug):
    """Individual program detail page"""
    program = get_object_or_404(Program, slug=slug, is_active=True)
    site_settings = SiteSettings.objects.first()

    # Get related programs
    related_programs = Program.objects.filter(
        is_active=True
    ).exclude(id=program.id).order_by('order')[:3]

    context = {
        'site_settings': site_settings,
        'program': program,
        'related_programs': related_programs,
    }

    return render(request, 'program_detail.html', context)


def enhanced_team(request):
    """Enhanced team page using new content management system"""
    site_settings = SiteSettings.objects.first()
    team_sections = PageSection.objects.filter(
        page='team',
        is_active=True
    ).prefetch_related('content_blocks').order_by('order')

    team_members = TeamMember.objects.filter(is_active=True).order_by('order')

    context = {
        'site_settings': site_settings,
        'team_sections': team_sections,
        'team_members': team_members,
    }

    return render(request, 'enhanced_team.html', context)


def enhanced_contact(request):
    """Enhanced contact page using new content management system"""
    site_settings = SiteSettings.objects.first()
    contact_sections = PageSection.objects.filter(
        page='contact',
        is_active=True
    ).prefetch_related('content_blocks').order_by('order')

    context = {
        'site_settings': site_settings,
        'contact_sections': contact_sections,
    }

    return render(request, 'enhanced_contact.html', context)


def search_content(request):
    """Search functionality for content"""
    query = request.GET.get('q', '')
    results = []

    if query:
        # Search in page sections
        section_results = PageSection.objects.filter(
            Q(title__icontains=query) |
            Q(heading__icontains=query) |
            Q(content__icontains=query),
            is_active=True
        )

        # Search in programs
        program_results = Program.objects.filter(
            Q(name__icontains=query) |
            Q(short_description__icontains=query) |
            Q(full_description__icontains=query),
            is_active=True
        )

        # Search in team members
        team_results = TeamMember.objects.filter(
            Q(name__icontains=query) |
            Q(position__icontains=query) |
            Q(bio__icontains=query),
            is_active=True
        )

        results = {
            'sections': section_results,
            'programs': program_results,
            'team': team_results,
            'query': query,
        }

    site_settings = SiteSettings.objects.first()
    context = {
        'site_settings': site_settings,
        'results': results,
        'query': query,
    }

    return render(request, 'search_results.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')