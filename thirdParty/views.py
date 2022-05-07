from django.http import JsonResponse
from django.shortcuts import render
from . import models


def authenticator(request, id, host):
    try:
        key = models.Id.objects.get(
            application_host=host,
            application_id=id,
        )
        # if it work; give user info:
        if request.user.is_authenticated:
            return JsonResponse(
                {"auth": True, "details": {
                    "username": request.user.username,
                    "first_name": request.user.first_name,
                    "last_name": request.user.last_name,
                }}
            )
        else:
            return JsonResponse({"auth": False})
    except:
        return render(request, "404.html")
