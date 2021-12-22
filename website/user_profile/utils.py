import random
import urllib.request
import datetime
import time
import pytz

from difflib import SequenceMatcher
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from .models import Profile


class ProfileMatcher:
    """
    A ProfileMatcher object contains the query and ratio_threshold
    """

    def __init__(self, query: str, ratio_threshold=0.36):
        """
        :param query: The keyword to be searched (str)
        :param ratio_threshold: The threshold ratio (float)
        :type query: str
        :type ratio_threshold: float
        """
        self.query = str(query).lower()
        self.ratio_threshold = ratio_threshold

    def matcher(self, obj):
        score = max(
            SequenceMatcher(None, obj.name.lower(), self.query).ratio(),
            -1
        )
        if score >= self.ratio_threshold:
            return score
        return 0

    def __str__(self):
        return 'ProfileMatcher object with query="{}", ratio_threshold={} .'.format(self.query, self.ratio_threshold)


def profilePicAdder():
    # print('running profile pic adder')
    qs = Profile.objects.all()
    messages = []
    tz = pytz.timezone(settings.TIME_ZONE)
    for profile in qs:
        messages.append(f"{datetime.datetime.now(tz=tz)}::Checking profile of {profile}")
        if not profile.image:
            full_path = f'media/images/{profile.user.username}.png'
            image_url = f"https://recursionnitd.in/static/image/profile_pic/{random.randint(1, 15)}.png"
            try:
                urllib.request.urlretrieve(image_url, full_path)

            except Exception as e:
                print(f"Failed to get DP for {profile.user}.\nError: {e}")
                messages.append(f"Failed to get DP for {profile.user}.\nError: {e}")
                continue
            profile.image = f"../{full_path}"
            profile.save()
            messages.append(f"{datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))}::Set dp for {profile}")

    # send_mail(
    #     subject="Logs for missing DP adding scheduler",
    #     message='\n'.join(messages),
    #     from_email=None,
    #     recipient_list=[
    #         'arin17bishwa@gmail.com',
    #     ]
    # )
    print('\n'.join(messages))


def DPAddScheduler():
    now_time = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
    # print(f"running DPAddScheduler() at {now_time}")
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    debug_time = now_time + datetime.timedelta(seconds=5)
    # print(f"remaining time: {debug_time - now_time}")
    runtime = datetime.datetime(2021, 12, 22, 23, 0, 0)
    runtime_aware = runtime.astimezone(pytz.timezone(settings.TIME_ZONE))
    scheduler.add_job(profilePicAdder, 'date', run_date=debug_time)
    scheduler.start()
