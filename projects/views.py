from django.shortcuts import render
from github import *
from .models import *


def projects(request):
    g = Github("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")

    for i in g.get_organization("RSAHDA").get_repos():
        project = Project(name=i.name, url=f"https://github.com/RSAHDA/{i.name}", description=i.description)

        try:
            Project.objects.get(name=i.name)
        except:
            project.save()

    return render(request, "projects.html", {
        "repos": Project.objects.all()
    })
