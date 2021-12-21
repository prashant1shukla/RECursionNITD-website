from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile'

    def ready(self):
        # print('starting ready() func')
        from .utils import DPAddScheduler
        DPAddScheduler()
