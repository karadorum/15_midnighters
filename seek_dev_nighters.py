import requests
import pytz
from datetime import datetime


<<<<<<< HEAD
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
=======
def get_number_of_pages():
    first_page = 1
    url = 'https://devman.org/api/challenges/solution_attempts'
    request_params = {'page': first_page}
    response = requests.get(url, request_params)
    number_of_pages = response.json()['number_of_pages']
    return number_of_pages


def load_attempts(pages):
    url = 'https://devman.org/api/challenges/solution_attempts'
    for page in range(1, pages):
        request_params = {'page': page}
        response = requests.get(url, request_params)
        json_api_page = response.json()['records']
        for attempt in json_api_page:
            yield attempt
>>>>>>> 1ba91e3ffc21b88583cd6844ba3eb7ed01aa4bba


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
<<<<<<< HEAD
    users = get_midnighters(load_attempts())
=======
    pages = get_number_of_pages()
    users = get_midnighters(load_attempts(pages))
>>>>>>> 1ba91e3ffc21b88583cd6844ba3eb7ed01aa4bba
    print('This users coding in the night:')
    for user in users:
        print(user)
