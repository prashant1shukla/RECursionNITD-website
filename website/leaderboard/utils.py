import time

from .models import Codeforces
from .leaderboard_scheduler.apis import CodeforcesAPI


def main():
    print('starting main()')
    forces = CodeforcesAPI()
    users = forces.getDataFromFile()
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


def CFPurifier():
    cf = CodeforcesAPI()
    cf.handlePurifier()
