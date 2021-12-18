from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    name = 'leaderboard'

    def ready(self):
        print('starting the purifier')
        from . import utils
        utils.CFPurifier()
