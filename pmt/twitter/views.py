from django.shortcuts import render
from django.http import JsonResponse
from django.middleware import csrf
from .models import Twitt 
from django.utils import timezone

import json

from django.views.decorators.csrf import csrf_exempt

def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'token': token})

@csrf_exempt
def index(request):
    if request.method == 'POST':
        add_twitt(request)
    twitts = list_all_twitts()
    return JsonResponse(twitts, safe=False)


def add_twitt(request):
    name = request.POST.get('name', '!')
    text = request.POST.get('text', '!')
    twitt = Twitt(name=name, text=text, twitt_date=timezone.now())
    twitt.save()


def list_all_twitts():
    return list(Twitt.objects.all().values())
    
