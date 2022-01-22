from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("logout/", views.sign_out, name="sign_out")
]
