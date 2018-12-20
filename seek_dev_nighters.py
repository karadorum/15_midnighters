import requests
import pytz
from datetime import datetime


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts'
    page = 1
    while True:
        request_params = {'page': page}
        response = requests.get(url, request_params)
        attempts = response.json()['records']
        number_of_pages = response.json()['number_of_pages']
        for attempt in attempts:
            yield attempt
        page += 1
        if page >= number_of_pages:
            break


def get_midnighters(attempts):
    midnighters = []
    for attempt in attempts:
        user_time = get_local_datetime(attempt)
        start_hour = 0
        end_hour = 6
        if start_hour <= user_time.hour <= end_hour:
            midnight_user = attempt.get('username')
            if midnight_user not in midnighters:
                midnighters.append(attempt.get('username'))
    return midnighters


def get_local_datetime(attempt):
    user_timezone = pytz.timezone(attempt.get('timezone'))
    user_time = datetime.fromtimestamp(attempt.get('timestamp'), tz=user_timezone)
    return user_time


if __name__ == '__main__':
    users = get_midnighters(load_attempts())
    print('This users coding in the night:')
    for user in users:
        print(user)
