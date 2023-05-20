from django.shortcuts import render
from github import *
from .models import *
import os


def projects(request):
    g = Github(os.environ.get("github_token"))

    for i in g.get_organization("RSAHDA").get_repos():
        project = Project(name=i.name, url=f"https://github.com/RSAHDA/{i.name}", description=i.description)

        try:
            Project.objects.get(name=i.name)
        except:
            project.save()

    return render(request, "projects.html", {
        "repos": Project.objects.all()
    })
