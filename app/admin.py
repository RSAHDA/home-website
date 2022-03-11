from django.contrib import admin
from .models import *


class blocked_ipAdmin(admin.ModelAdmin):
    list_display = ['sus_ips']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['anouncement']


class UserJobAdmin(admin.ModelAdmin):
    list_display = ["username", "job_title", "repo"]
    list_filter = ["job_title", "repo"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "group_of",
        "project",
        "mean_age",
        "leader_name",
        "leader_age",
        "expected_profit_per_week",
        "needs",
    ]
    list_filter = ["name", 'project']


class EarningAdmin(admin.ModelAdmin):
    list_display = ["revenue", "expense"]


admin.site.register(blocked_ip, blocked_ipAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(UserJob, UserJobAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Earning, EarningAdmin)
