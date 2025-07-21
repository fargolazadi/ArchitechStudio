from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('name','subject','published_date')
    list_filter = ['email']
    search_fields = ['name']

admin.site.register(Contact,ContactAdmin)