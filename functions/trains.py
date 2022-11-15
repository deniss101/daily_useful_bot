import requests
from datetime import date
from os import environ

token = environ.get('ya_rasp_api')

date_input = str(date.today())
transport_type = 'suburban'
station_from = 's9874963'
station_to = 'на Москву'


def trains_request():
    answer = requests.get(
        f'https://api.rasp.yandex.net/v3.0/schedule/'
        f'?apikey={token}'
        f'&station={station_from}'
        f'&date={date_input}'
        f'&transport_types={transport_type}'
        f'&direction={station_to}')
    return str(answer.json()['station'])


if __name__ == "__main__":
    print(trains_request())
