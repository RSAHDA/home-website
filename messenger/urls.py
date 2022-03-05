from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name="inbox_display"),
    path('create/', views.create_message, name="create_message"),
    path('trash/', views.trash, name="trash_display"),
    path('<int:id>', views.view_message, name="message_display"),
    path('delete/<int:id>/<int:permanent_delete>', views.delete_message, name="delete_message"),
]
