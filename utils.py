from django.core.mail import send_mail
from django.conf import settings


def notify_admin(subject, message):
    send_mail(
        subject, message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=True,
    )