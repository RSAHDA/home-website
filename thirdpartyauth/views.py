from django.shortcuts import render
from django.http import JsonResponse
from . import models


def authenticator(request, id, host):
    try:
        key = models.Id.objects.get(
            application_host=host,
            application_id=id,
        )
        # if it works, give user info:
        return JsonResponse(
            {"auth": True, "details":{
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }})
    except:
        return JsonResponse({"auth": False})
