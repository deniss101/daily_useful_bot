import requests
from datetime import date, datetime
from os import environ

token = environ.get('ya_rasp_api')

date_input = str(date.today())
transport_type = 'suburban'
now = datetime.now()
current_time = now.strftime("%H:%M")

#station_from = 's9874963'
#station_to = 's9600741'


def trains_request2():
    answer = requests.get(
        f'https://api.rasp.yandex.net/v3.0/schedule/'
        f'?apikey={token}'
        f'&from={station_from}'
        f'&to={station_to}'
        f'&date={date_input}'
        f'&transport_types={transport_type}')
        #f'&direction={station_to}')
    return answer.json()


def trains_request(station_from, station_to):
    answer = requests.get(
        f'https://api.rasp.yandex.net/v3.0/search/'
        f'?apikey={token}'
        f'&format=json'
        f'&from={station_from}'
        f'&to={station_to}'
        f'&lang=ru_RU'
        f'&page=1'
        f'&transport_types={transport_type}'
        f'&date={date_input}'
        f'&limit=200')
    data = answer.json()
    path = (data['search']['from']['title'] + ' - ' + data['search']['to']['title'] + '\n')
    times = ''
    count = 0
    for i in data['segments']:
        if i['departure'].replace(date_input + 'T', '').replace(':00+03:00', '') > current_time and count < 100:
            times += (i['departure'].replace(date_input + 'T', '').replace(':00+03:00', '') + '\n')
            count += 1

    return path + times


if __name__ == "__main__":
    print(trains_request('s9874963', 's9600741'))


    '''if time < current time:
    offset += 1
    '''