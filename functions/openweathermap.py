import requests
from os import environ

token = environ.get('openweathermap')
city_input = 'Москва'


def weather_request():
    answer = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={token}&lang=ru&units=metric')
    city = answer.json()['name']
    temp = 'Температура: ' + str((round(answer.json()['main']['temp'], 1))) + 'C'
    wind = 'Ветер: ' + str(answer.json()['wind']['speed']) + 'м/с'
    description = answer.json()['weather'][0]['description'].capitalize()
    return '\n'.join([city, temp, wind, description])


if __name__ == "__main__":
    print(weather_request())
    '''print(answer.json())
    print(answer.json()['name'])
    print('Температура: ', (round(answer.json()['main']['temp'], 1)), 'C', sep='')
    print('Ветер: ', answer.json()['wind']['speed'], 'м/с', sep='')
    print(answer.json()['weather'][0]['description'].capitalize())'''
