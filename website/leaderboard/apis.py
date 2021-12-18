from typing import List
from django.conf import settings
from os import path
import user_profile.models as user_profile_models
import json
import requests


class CodeforcesAPI:
    def __init__(self):
        self.base_url = 'https://codeforces.com/api/user.info?handles='

    @staticmethod
    def getDataFromFile() -> List[dict]:
        print("Reading data from response.json")
        with open(path.join(settings.BASE_DIR, 'leaderboard', 'response.json')) as file:
            js = json.load(file)
        return js['result']

    def getResponse(self, usernames=None) -> List[dict]:
        if not usernames:
            usernames = self.getUsers()
        names = ';'.join(usernames)
        url = self.base_url + names
        res = requests.get(url)
        print(f"Response status: {res.status_code}")
        if not res.ok:
            print('API fetch broke')
            return []
        res = res.json()
        with open(path.join(settings.BASE_DIR, 'leaderboard', 'response.json'), 'w') as file:
            json.dump(res, file, indent=4)
        return res['result']

    @staticmethod
    def getUsers() -> List[str]:
        with open(path.join(settings.BASE_DIR, 'leaderboard', 'usernames.json')) as file:
            js = json.load(file)
        usernames = js['usernames']
        return usernames

    def individualRequest(self, handle: str) -> json:
        print(f"requesting for {handle}")
        if not handle:
            return {}
        url = self.base_url + handle
        res = requests.get(url)
        if res.status_code == 400:
            return {}
        return res.json()

    @staticmethod
    def UrlToHandle(url: str) -> str:
        if not url:
            return ''
        arr = url.split('/')
        handle = arr[-1]
        return handle

    def handlePurifier(self):
        print('running purifier()')
        profiles = user_profile_models.Profile.objects.all()
        for profile in profiles:
            cf_url = profile.url_Codeforces
            if cf_url and not self.isValidHandle(cf_url):
                profile.url_Codeforces = ''
                print(f"changing {profile}")
                profile.save()

    def isValidHandle(self, obj: str, is_url=True) -> bool:
        if not obj:
            return False
        if is_url:
            handle = self.UrlToHandle(obj)
        else:
            handle = obj
        return self.individualRequest(handle)

    def __str__(self):
        return 'Codeforces API'
