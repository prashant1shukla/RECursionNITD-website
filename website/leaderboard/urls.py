from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    leaderboardCFView
)
app_name = "leaderboard"

urlpatterns = [
    path('codeforces/', leaderboardCFView, name='leaderboard_home'),
]
