from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
    list_filter = ["name"]


admin.site.register(Project, ProjectAdmin)
