from django.contrib import admin
from .models import I_m, Projects


@admin.register(I_m)
class I_mAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']