from django.contrib import admin
from .models import *


class blocked_ipAdmin(admin.ModelAdmin):
    list_display = ['sus_ips']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['anouncement']


admin.site.register(blocked_ip, blocked_ipAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
