import re
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
import app.views

def index(request):
    if not request.user.is_authenticated:
        views.index()
    else:
        return redirect("/home/")
