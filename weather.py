# Your API key is 4dff31c855f6108ab6652907f07d9060

#
import pprint
import requests
from datetime import datetime
import json

wwa_lat = 52.2319581
wwa_lon = 21.0067249
API = "4dff31c855f6108ab6652907f07d9060"     # SKASOWAĆ

historia_pogody = {}

# API_KEY = sys.argv[1]
# API_url = F"http://api.openweathermap.org/data/2.5/forecast?lat={52.2319581}&lon={21.0067249}&appid={API}"
API_url = F"https://api.openweathermap.org/data/2.5/onecall?lat={wwa_lat}&lon={wwa_lon}&exclude=hourly,minutely,alerts,current&appid={API}"

odpowiedz = requests.get(API_url)

# pprint.pprint(odpowiedz.json())             # pprint.pprint(odpowiedz.json()["list"][3]["weather"])


zapytanie = odpowiedz.json()                # zapytanie = odpowiedz.json()["list"][1]["weather"]





for it in zapytanie["daily"]:
    data = datetime.fromtimestamp(it["dt"]).date()
    dzien = str(data)

    rain = it.get("rain")
    # rain = glowny.get("rain")
    if rain:
        historia_pogody[dzien] = ["pada"]
    else:
      historia_pogody[dzien] = ["nie pada"]
print(historia_pogody)

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

