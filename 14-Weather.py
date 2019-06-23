import requests
# city = "Macerata"
city = input('Введіть місто(En): ')
appid = "47212252e5b0293b1e53348aa194bdb3"
while True:
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                      params={'q': city, 'units': 'metric', 'lang': 'ua', 'APPID': appid})
        data = res.json()
        print('Місто: ', data['name'],'('+str(data['sys']['country'])+')', '\n')
        print("* Хмарність:", data['weather'][0]['description'])
        print("* Температура повітря:", str(data['main']['temp']) + '°С')
        print("* Температура повітря від ", str(data['main']['temp_min'])+'°С', 'до', str(data['main']['temp_max'])+'°С')
        print('* Вологість: ', str(data['main']['humidity']) + '%', )
        print('* Вітер: ', str(data['wind']['speed']) + 'km/год', )
        break

    except Exception:
        print("Такого міста немає")
        city = input('Введіть місто(En): ')




