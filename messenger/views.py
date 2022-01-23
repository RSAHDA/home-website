from django.shortcuts import render, redirect
import managment


def messages(request):
    if request.user.is_authenticated:
        return render(request, "messages.html", {
            'messages': managment.load_mails(request)
        })
    else:
        return render(request, "404.html")


def display_message(request, message):
    if request.user.is_authenticated:

        loaded_messages = managment.load_mails(request)
        filtered = loaded_messages.filter(
            subject=message
        )

        return render(request, "message.html", {
            'details': filtered
        })
    else:
        return render(request, "404.html")
