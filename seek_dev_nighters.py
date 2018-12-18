import requests
import pytz
from datetime import datetime



def get_number_of_pages():
    first_page = 1
    url = 'https://devman.org/api/challenges/solution_attempts/?page={}'.format(first_page)
    response = requests.get(url)
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
    user_time = datetime.fromtimestamp(attempt.get('timestamp'), tz= user_timezone)
    return user_time

if __name__ == '__main__':
    pages = get_number_of_pages()
    users =  get_midnighters(load_attempts(pages))
    print('This users never sleep:')
    for user in users:
        print(user)
