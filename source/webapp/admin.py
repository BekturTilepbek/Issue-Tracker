from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'complete_date']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'detailed_description', 'status', 'complete_date']


admin.site.register(Task, TaskAdmin)
