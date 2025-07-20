from django.contrib import admin
from .models import Event
from unfold.admin import ModelAdmin

@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
