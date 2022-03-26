# Your API key is 4dff31c855f6108ab6652907f07d9060

# OPEN WEATHER:


import pprint
import requests
from datetime import datetime
import json
import csv
import sys
import os

API_ARGV = sys.argv[1]
data_argv = sys.argv[2]

wwa_lat = 52.2319581
wwa_lon = 21.0067249
API = "4dff31c855f6108ab6652907f07d9060"     # SKASOWAĆ

pogoda = {}


API_url = F"https://api.openweathermap.org/data/2.5/onecall?lat={wwa_lat}&lon={wwa_lon}&exclude=hourly,minutely,alerts&appid={API_ARGV}"


if os.stat("historia_pogody.json").st_size > 0: #sprawdza, czy plik jest pusty czy nie
    print("Sprawdzam historię...")
    with open("historia_pogody.json", "r") as plik:
        sprawdzenie_historii = json.load(plik)
        wyszukiwanie = sprawdzenie_historii.get(data_argv)
        if wyszukiwanie:
            print(F"{data_argv}: {wyszukiwanie}")
            exit()
        else:
            print("Wysyłam zapytanie")

else:
    print("Wysyłam zapytanie")




odpowiedz = requests.get(API_url)
# pprint.pprint(odpowiedz.json())             # pprint.pprint(odpowiedz.json()["list"][3]["weather"])
zapytanie = odpowiedz.json()                # zapytanie = odpowiedz.json()["list"][1]["weather"]


for it in zapytanie["daily"]:
    data_format = datetime.fromtimestamp(it["dt"]).date()   # przeszukiwanie po dacie
    dzien = str(data_format)      #zmiana formatu na ludzki
    if dzien == data_argv:
        rain = it.get("rain")
        if rain:
            print(F"{data_argv}: pada")
            pogoda[dzien] = ["pada"]
        else:
            pogoda[dzien] = ["nie pada"]
            print(F"{data_argv}: nie pada")

if data_argv not in pogoda:
    print("Brak informacji. Maksymalne wyszukiwanie to 7 dni od daty dzisiejszej")
    exit()


try:
    with open("historia_pogody.json", "r") as plik:
        aktualizacja_slownika = json.load(plik)
        aktualizacja_slownika.update(pogoda)        # wypakowaywanie słownika z pliku i aktualizowanie o dane ze słownika "pogoda"

    with open("historia_pogody.json", "w") as plik:  # zapisywanie uaktualniownego słownika do pliku
        json.dump(aktualizacja_slownika, plik, sort_keys=True, indent=4, separators=(',', ': '))
        # json.dump(aktualizacja_slownika, plik, sort_keys=True, indent=4, separators=(',', ': '))
except:
    with open("historia_pogody.json", "w") as plik:
        json.dump(pogoda, plik, sort_keys=True, indent=4, separators=(',', ': '))
        # json.dump(pogoda, plik, sort_keys=True, indent=4, separators=(',', ': '))












# for it in zapytanie["daily"]:
#     data = datetime.fromtimestamp(it["dt"]).date()
#     dzien = str(data)
#
#     rain = it.get("rain")
#     if rain:
#         pogoda[dzien] = ["pada"]
#     else:
#       pogoda[dzien] = ["nie pada"]
#
# with open("historia_pogody.json", "a", newline='') as plik:
#     json.dump(pogoda, plik, sort_keys=True, indent=4, separators=(',', ': '))














# print(pogoda)

# zapytanie = odpowiedz.json()["list"]
# print(len(zapytanie))



# for weather in zapytanie

# for listy in zapytanie:
#   print(len(listy))

# with open('data.json', 'w') as plik:
#   json.dump(zapytanie, plik, indent=4, sort_keys=True, separators=(",", ':'))



# print(odpowiedz.url)    #sprawdza, jakie zapytanie poszło do api


# miasto = zapytanie["city"]["name"]
# daytime = zapytanie["list"][1]["dt_txt"]
# daytime_x = zapytanie["list"][12]["dt_txt"]
# pogoda = zapytanie["list"][23]["weather"][0]["main"]
# pogoda = zapytanie["list"][23]["weather"][0]["main"]




# daytime2 = zapytanie["list"]["clouds"]["dt_txt"]

# print(zapytanie)      # w jednym ciągu
# print(daytime_x)
# print(pogoda)

#
# from datetime import datetime, timedelta
# date = datetime.fromtimestamp(1648371600).date()
# print(date + timedelta(days=2))


# # jeżlei chcemy zrzucić plik do .json to
#
# deszcz = {"2022-03-10": "nie pada", "2022-03-11" : "pada"}
#
# requested_date = "2022-03-10" [sys.argv[1]]
# if requested_date in historia_pogody:
#     print(historia_pogody[requested_date])


# import json
# from datetime import datetime
#
# jjj = []
#
# moj_json = json.load(open("data.json", "r"))  # Tu load a nie loads :)
#
# for x in moj_json["list"]:
#     data = datetime.fromtimestamp(x["dt"]).date()
#
# for y in moj_json["list"]:
#     if y in moj_json["list"][y]["weather"] == "main":
#         print("yest")
#     else:
#         print("nie ma")



    # print(data)

'''''''''
### ZADANIE ###

można zapisywać informacje z API w .csv lub .json (do wyboru)

strona RapidApi: darmowe i płatne api do pobierania rzeczy


https://openweathermap.org/forecast5
## up to api: najpierw trzeba podać nawę miasta i api wypluwa szerokość długość geograficzną: mozna szerkość dla miasta spisać
# Examples of Api calls: przykład:
rejestracja i dostaniemy klucz do API

import sys

API_KEY = sys.argv[1]
api_url = f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

request.get(api_url)

biblioteka daytime i timedelta (dodawanie dni)

rozwiązanie musi mieć weather.py i equirements.txt (a nie venv)

api mają limity ile  mozna zrobić zapytań

pobieranie najłatwiej zrobić w .json (klucz: dzień, wartość: pada/nie pada)
ładujemy pusty .json i patrzymy dla jakiego dnia ktoś chce pobrać pogodę
jeżeli podał datę wcześniejszą niż w historii to nie wiem

czasami w ogóle parametr deszcz się nie pojawia, więc stosujemy .get
jeżeli nie ma tego parametru to go nie szczytujemy

w tym openweather api w pliku json dt to daytime zrobiony jako timestamp:
from datetime import datetime
date = datetime.fromtimestamp(1647345600).date()
print(date)

jeżlei chcemy zrzucić plik do .json to

{"2022-03-10": "nie pada", "2022-03-10" : "pada"}

requested_date = "2022-03-10" [sys.argv[1]]
if requested_date in historia_pogody:
print(historia_pogody[requested_date])

else:
print("robię zapytanie do API")





#### WARSZTATY  ####


'''''''''

