from django.contrib import admin
from .models import *


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['message']


admin.site.register(SentMail, MessagesAdmin)
