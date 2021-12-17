from django.shortcuts import render, HttpResponse
from .leaderboard_scheduler.utils import CFUpdater


# Create your views here.

def view(request):
    CFUpdater()
    return HttpResponse('hi')
