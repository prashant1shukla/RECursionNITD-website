import time

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from leaderboard.apis import CodeforcesAPI
from leaderboard.models import Codeforces


def CFUpdater():
    print('running CFUpdater()')
    forces = CodeforcesAPI()
    users = forces.getResponse()
    current_time = time.time()
    for user in users:
        handle = user['handle']
        is_active = (current_time - (user.get('lastOnlineTimeSeconds', 0))) < (31 * 24 * 3600)
        obj, created = Codeforces.objects.get_or_create(
            username=handle,
            first_name=user.get('firstName', ''),
            last_name=user.get('lastName', ''),
            current_rating=user.get('rating', 0),
            max_rating=user.get('maxRating', 0),
            is_active=is_active
        )
        if created:
            print(obj)


def startUpdate():
    print('running startUpdate()')
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_job(CFUpdater, 'interval', seconds=20, replace_existing=True, id='CF_001')
    scheduler.start()
