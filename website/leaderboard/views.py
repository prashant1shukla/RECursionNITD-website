from django.shortcuts import render, HttpResponse
from .leaderboard_scheduler.utils import CFUpdater
from leaderboard.models import Codeforces


# Create your views here.

def view(request):
    CFUpdater()
    return HttpResponse('hi')


def leaderboardHomeView(request):
    context = {
        'profiles': Codeforces.objects.all()
    }
    return render(request, 'leaderboardHome.html', context)
