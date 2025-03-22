from django.contrib import admin
from .models import Entry

# Register your models here
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display the title of the entry in the admin list view
    search_fields = ('title',)  # Add a search bar to search entries by title

