
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Event, EventCategory, EventComment, EventAttendee
from django.contrib import messages

def event_list(request):
    now = timezone.now()
    
    # Get all upcoming events
    events = Event.objects.filter(date__gte=now).order_by("-date")
    featured_events = Event.objects.filter(featured=True, date__gte=now)[:6]
    categories = EventCategory.objects.filter(active=True)
    
 

    # Get filter parameters
    event_type = request.GET.get('type', 'all')
    query = request.GET.get("q")
    category = request.GET.get("category")

    # Apply filters
    if event_type != 'all':
        events = events.filter(event_type=event_type.upper())
    
    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    if category:
        events = events.filter(category__slug=category)

    # Pagination
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    context = {
        "events": events,
        "featured_events": featured_events,
        "categories": categories,
        "selected_type": event_type,
        "query": query,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    comments = EventComment.objects.filter(event=event, active=True)
    
    # Get related events based on event type
    related_events = Event.objects.filter(
        event_type=event.event_type
    ).exclude(id=event.id).distinct()[:6]

    if request.method == "POST":
        form_type = request.POST.get('form_type')
        
        if form_type == 'comment':
            # Handle comment submission
            name = request.POST.get("name")
            comment = request.POST.get("comment")
            email = request.POST.get("email")

            EventComment.objects.create(
                name=name,
                email=email,
                comment=comment,
                event=event
            )
            messages.success(request, f"Thanks {name}, your comment has been posted!")
            
        elif form_type == 'attendance':
            # Handle attendance confirmation
            name = request.POST.get("attendee_name")
            email = request.POST.get("attendee_email")
            phone = request.POST.get("attendee_phone")
            
            try:
                EventAttendee.objects.create(
                    event=event,
                    name=name,
                    email=email,
                    phone=phone
                )
                messages.success(request, f"Thank you {name}! Your attendance has been confirmed.")
            except:
                messages.error(request, "You have already registered for this event.")

    context = {
        "event": event,
        "comments": comments,
        "related_events": related_events,
    }
    return render(request, 'events/event_detail.html', context)

