import json
import time
import requests
import os.path
import concurrent.futures
from typing import List
from django.conf import settings
from .models import StopStalk


class StopStalkAPI:
    def __init__(self):
        self.__name = 'StopStalkAPI'
        self.base_url_profile = 'https://www.stopstalk.com/user/profile.json/'
        self.base_url_submissions = 'https://www.stopstalk.com/user/get_stopstalk_user_stats.json?user_id={}&custom={}'

    @staticmethod
    def getHandlesFromJson() -> List:
        with open(os.path.join(settings.BASE_DIR, 'leaderboard', 'handles.json')) as file:
            js = json.load(file)
        handles = [user[1] for user in js['users']]
        return handles

    def getStopStalkProfile(self, handle: str):
        url = self.base_url_profile + handle
        res = requests.get(url)
        js = res.json()
        return js

    def updateSubmissions(self, user_id: int, custom=False):
        sites = ['CodeChef', 'CodeForces', 'Spoj']
        submission_data = self.getSubmissionsFromID(user_id=user_id, custom=js['custom'])
        solved_counts = {
            i: submission_data['solved_counts'].get(i, 0) for i in sites
        }
        obj = StopStalk.objects.update(
            stopStalk_id=user_id,
            codechef_solved=solved_counts[sites[0]],
            codeforces_solved=solved_counts[sites[1]],
            spoj_solved=solved_counts[sites[2]],
            total_solved=submission_data['solved_problems_count'],
        )

    def createUpdateProfile(self, handle: str):
        js = self.getStopStalkProfile(handle)
        sites = ['CodeChef', 'CodeForces', 'Spoj']
        urls = {
            i: '' if js['profile_urls'][i] == 'NA' else js['profile_urls'][i] for i in sites
        }
        submission_data = self.getSubmissionsFromID(user_id=js['user_id'], custom=js['custom'])
        solved_counts = {
            i: submission_data['solved_counts'].get(i, 0) for i in sites
        }
        obj, created = StopStalk.objects.update_or_create(
            username=handle,
            name=js['name'],
            stopStalk_id=js['user_id'],
            codechef_url=urls[sites[0]],
            codeforces_url=urls[sites[1]],
            spoj_url=urls[sites[2]],
            codechef_solved=solved_counts[sites[0]],
            codeforces_solved=solved_counts[sites[1]],
            spoj_solved=solved_counts[sites[2]],
            total_solved=submission_data['solved_problems_count'],
            custom=js['custom'],
        )

        if created:
            print(obj)

    def getSubmissionsFromID(self, user_id: int, custom=False):
        url = self.base_url_submissions.format(user_id, custom)
        res = requests.get(url)
        js = res.json()
        return js


def func():
    a = StopStalkAPI()
    handles = a.getHandlesFromJson()
    start = time.perf_counter()
    for handle in handles:
        a.createUpdateProfile(handle)
    end = time.perf_counter()
    print(f"Time taken for non-threaded: {end - start} secs")


def funcThreaded(threads=20):
    a = StopStalkAPI()
    handles = a.getHandlesFromJson()
    start = time.perf_counter()
    print(f"No.of handles: {len(handles)}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(a.createUpdateProfile, handles)
        workers = executor._max_workers
    end = time.perf_counter()
    print(f"Time taken for threaded({workers} threads): {end - start} secs")


def updateFunc(threads=20):
    api = StopStalkAPI()
    current_profiles = StopStalk.objects.values_list('user_id', 'custom')
    start = time.perf_counter()
    print(f"No.of handles: {len(current_profiles)}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(api.updateSubmissions, current_profiles)
        workers = executor._max_workers
    end = time.perf_counter()
    print(f"Time taken for update threaded({workers} threads): {end - start} secs")
