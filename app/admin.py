from django.contrib import admin
from .models import *


class blocked_ipAdmin(admin.ModelAdmin):
    list_display = ['sus_ips']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['anouncement']


class UserJobAdmin(admin.ModelAdmin):
    list_display = ["username", "job_title", "repo"]
    list_filter = ["job_title", "repo"]


admin.site.register(blocked_ip, blocked_ipAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(UserJob, UserJobAdmin)
