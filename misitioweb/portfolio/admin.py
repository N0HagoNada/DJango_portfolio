from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created','url')
    ordering = ('title', 'created')
    search_fields = ('title','content','author__username')
    date_hierarchy = 'updated'
    
admin.site.register(Project, ProjectAdmin)