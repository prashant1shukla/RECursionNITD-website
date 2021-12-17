from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    name = 'leaderboard'

    def ready(self):
        print('starting the update')
        from .leaderboard_scheduler import utils
        utils.startUpdate()
