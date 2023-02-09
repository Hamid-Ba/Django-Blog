from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from time import sleep
from . import tasks


def send_email(request):
    tasks.send_email.delay()
    return HttpResponse("<h1>EMAIL HAS BEEN SENT</h1>")
