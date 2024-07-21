from django.contrib import admin

from webapp.models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'created_at', 'updated_at']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'detailed_description', 'status', 'types']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    fields = ['name']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    fields = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'started_at']
    list_display_links = ['id', 'name']
    fields = ['name', 'description', 'started_at', 'ended_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
