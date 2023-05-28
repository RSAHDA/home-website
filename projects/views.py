from django.shortcuts import render
from github import *
from .models import *
import os


def get_token():
    encode = ' _qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    encode = list(encode)
    decoded = ''
    t = '16 17 11 1 47 50 31 52 10 3 5 60 47 8 49 47 39 22 36 56 32 22 14 14 3 59 16 60 50 6 13 3 50 14 28 22 24 41 30 33'
    for i in t.split():
        decoded += encode[int(i)]
    return decoded


def projects(request):
    ## TODO:
    # g = Github(get_token())

    # for i in g.get_organization("RSAHDA").get_repos():
    #     project = Project(name=i.name, url=f"https://github.com/RSAHDA/{i.name}", description=i.description)

    #     try:
    #         Project.objects.get(name=i.name)
    #     except:
    #         project.save()

    # return render(request, "projects.html", {
    #     "repos": Project.objects.all()
    # })
    return render(request, "error.html")
