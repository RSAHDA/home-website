from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name="inbox_display"),
    path('<slug:message>', views.display_message, name="message_display"),
]
