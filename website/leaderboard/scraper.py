import json
import requests


def main():
    url = "https://www.stopstalk.com/leaderboard.json?q=National+Institute+of+Technology%2C+Durgapur"

    payload = {}

    res = requests.get(url, headers={}, data=payload)
    js = res.json()
    with open('handles.json', 'w') as file:
        json.dump(js, file, indent=4)


if __name__ == '__main__':
    main()
