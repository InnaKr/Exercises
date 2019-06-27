import requests
import argparse

# lang = input('Введіть мову пошуку(En/Ua/Ru): ')
# city = input('Введіть місто(En): ')

appid = "47212252e5b0293b1e53348aa194bdb3"

def show_weather(lang,city):
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'q': city, 'units': 'metric', 'lang': lang, 'APPID': appid})
    data = res.json()
    print('Місто: ', data['name'],'('+str(data['sys']['country'])+')', '\n')
    print("* Хмарність:", data['weather'][0]['description'])
    print("* Середня температура повітря:", str(data['main']['temp']) + '°С')
    print("* Температура від ", str(data['main']['temp_min'])+'°С', 'до', str(data['main']['temp_max'])+'°С')
    print('* Вологість: ', str(data['main']['humidity']) + '%', )
    print('* Вітер: ', str(data['wind']['speed']) + 'km/год', )

# show_weather("en", "london")

parser = argparse.ArgumentParser(description='Введіть мову пошуку та місто:')
parser.add_argument('-l', action="store", dest="lang", default="en", type=str)
parser.add_argument('-c', action="store", dest="city", type=str)

args = parser.parse_args()

show_weather(args.lang, args.city)






