from django.contrib import admin
from .models import *


class ipAdmin(admin.ModelAdmin):
    list_display = ['location']
    list_filter = ['location']


class blocked_ipAdmin(admin.ModelAdmin):
    list_display = ['sus_ips']


admin.site.register(ip, ipAdmin)
admin.site.register(blocked_ip, blocked_ipAdmin)
