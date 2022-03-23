from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("logout/", views.sign_out, name="sign_out"),
    path("home/", views.home, name="home_page"),
    path("api/profit_data/<int:salary>", views.profitAPI, name="profit_data_API"),
    path("add_todo/", views.add_todo, name="todo_add_display"),
    path("delete_todo/<int:pk>/", views.delete_todo, name="delete_todo_display"),
    path("report/", views.report, name="report_display"),
]
