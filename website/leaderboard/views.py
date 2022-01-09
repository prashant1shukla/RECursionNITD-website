from django.shortcuts import render, HttpResponse
from .leaderboard_scheduler.utils import CFUpdater
from leaderboard.models import Codeforces


# Create your views here.

def leaderboardCFView(request):
    context = {
        'profiles': Codeforces.objects.all()
    }
    return render(request, 'leaderboardCF.html', context)
