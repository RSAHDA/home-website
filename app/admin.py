from django.contrib import admin
from .models import *


class ipAdmin(admin.ModelAdmin):
    list_display = ['location']
    list_filter = ['location']


admin.site.register(ip, ipAdmin)
