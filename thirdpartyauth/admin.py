from django.contrib import admin
from .models import *

class IdAdmin(admin.ModelAdmin):
    list_display = ["application_host", "application_id"]

admin.site.register(Id, IdAdmin)
