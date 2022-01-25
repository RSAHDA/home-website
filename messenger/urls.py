from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name="inbox_display"),
    path('create/', views.create_message, name="create_message_display"),
    path('<int:id>', views.view_message, name="display_message_display"),
]
