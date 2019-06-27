import requests
import argparse

appid = "47212252e5b0293b1e53348aa194bdb3"

def show_weather(lang, city):
    try:
        param = {'lang': lang, 'q': city, 'units': 'metric', 'APPID': appid}
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                   params=param)
        data = res.json()
        print('Місто: ', data['name'], '(' + str(data['sys']['country']) + ')', '\n')
        print("* Хмарність:", data['weather'][0]['description'])
        print("* Середня температура повітря:", str(data['main']['temp']) + '°С')
        print("* Температура від ", str(data['main']['temp_min']) + '°С', 'до',
                      str(data['main']['temp_max']) + '°С')
        print('* Вологість: ', str(data['main']['humidity']) + '%', )
        print('* Вітер: ', str(data['wind']['speed']) + 'km/год', )


    except Exception:
            print("Такого міста немає")



parser = argparse.ArgumentParser(description='Введіть мову пошуку та місто:')
parser.add_argument('-l', action="store", dest="lang", default="en", type=str)
parser.add_argument('-c', action="store", dest="city", type=str)

args = parser.parse_args()

show_weather(args.lang, args.city)
