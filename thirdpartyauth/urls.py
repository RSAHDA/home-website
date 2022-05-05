from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>2022<str:host>/', views.authenticator),
]
