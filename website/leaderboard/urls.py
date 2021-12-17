from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    view
)
app_name = "leaderboard"

urlpatterns = [
    path('', view, name='leaderboard_home'),
]
