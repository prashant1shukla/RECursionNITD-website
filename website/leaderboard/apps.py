from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    name = 'leaderboard'

    def ready(self):
        from leaderboard.api import func, funcThreaded
        print('ready')
        # func()
        # funcThreaded()
