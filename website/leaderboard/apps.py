from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    name = 'leaderboard'

    def ready(self):
        print('starting the task')
        from . import utils as base_utils
        from .leaderboard_scheduler import utils as utils
        # base_utils.CFPurifier()
        utils.startUpdate()
