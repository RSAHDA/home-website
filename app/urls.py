from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("logout/", views.sign_out, name="sign_out"),
    path("home/", views.home, name="home_page"),
    path("api/profit_data/", views.profitAPI, name="profit_data_API"),
]
