import json
import requests
from typing import List


class StopStalkAPI:
    def __init__(self):
        self.__name = 'StopStalkAPI'
        self.base_url_profile = 'https://www.stopstalk.com/user/profile.json/'

    @staticmethod
    def getHandlesFromJson() -> List:
        with open('handles.json') as file:
            js = json.load(file)
        handles = [user[1] for user in js['users']]
        return handles

    def getUserIDFromHandle(self, handle: str) -> int:
        url = self.base_url_profile + handle
        res = requests.get(url)
        js = res.json()
        return js['id']


def main():
    a = StopStalkAPI()
    h = a.getHandlesFromJson()
    print(*h, sep='\n')


if __name__ == '__main__':
    main()
