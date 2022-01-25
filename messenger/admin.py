from django.contrib import admin
from .models import *


class SentMailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'send_to', 'from_whom', 'is_in_trash', 'message_id']
    list_filter = ['send_to', 'from_whom']


admin.site.register(SentMail, SentMailAdmin)
