from messenger.models import *
import random


def send_mail(send_to, request, html_message, message, subject):
    send_from = request.user.username
    message_id = random.randint(0, 1 * (10 ** 15))
    new_message = SentMail(
        send_to=send_to,
        from_whom=send_from,
        message=message,
        html=html_message,
        subject=subject,
        is_in_trash=False,
        message_id=message_id,
    )
    new_message.save()


def load_mails(request):
    username = request.user.username
    mails = SentMail.objects.filter(
        send_to=username,
        is_in_trash=False,
    )
    return mails
