import requests
import tkinter

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Tallinn&appid=e4ad5086a9b72ea03cd03a2934b65067&units=metric&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']

        return (f"Weather in Tallinn: {description}\n"
                f"Temp: {temp}°C\n"
                f"humidity: {humidity}%\n"
                f"pressure: {pressure} hPa")
    else:
        return "Error: failed to retrieve weather data"


def get_character_info(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        status = data['status']
        species = data['species']
        origin = data['origin']['name']
        location = data['location']['name']
        image = data['image']

        return (f"Имя: {name}\n"
                f"Статус: {status}\n"
                f"Вид: {species}\n"
                f"Родная планета: {origin}\n"
                f"Текущее местоположение: {location}\n"
                f"Ссылка на изображение: {image}")
    else:
        return "Error: failed to retrieve weather data"


def get_all_characters():
    url = "https://rickandmortyapi.com/api/character"
    characters = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for character in data["results"]:
                characters.append(f"{character['id']} - {character['name']}")

            # Проверяем, есть ли следующая страница
            url = data["info"]["next"]
        else:
            return "Error: failed to retrieve weather data"

    return "\n".join(characters)




flag = 1
while flag == True:
    print('What do u want?')
    print('1 - weather in Tallinn')
    print('2 - Rick and Morty character data')
    print('0 - exit')
    data = int(input())
    if data == 1:
        print('')
        print(get_weather())
        print('')
    elif data == 2:
        print('You want to see a list of character ids? y or n')
        f = 1;
        data2 = 1
        while f == True:
            data1 = input()
            if data1 == 'y':
                print(get_all_characters())
                print('Write id of character')
                data2 = int(input())
                f = 0
            elif data1 == 'n':
                print('Write id of character')
                data2 = int(input())
                f = 0
            else: print("only y or n")
        print(get_character_info(data2))
    elif data == 0:
        flag = 0

    else:
        print('Only 1,2,3,0 supported functions')
