from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/<str:host>/', views.authenticator),
]
