from django.http import HttpResponse
from . import tasks


def send_email(request):
    tasks.send_email.delay()
    return HttpResponse("<h1>EMAIL HAS BEEN SENT</h1>")
