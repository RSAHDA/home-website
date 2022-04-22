from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from github import *
from .models import *

@csrf_exempt
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
