import os
import sys
import json
import requests
from datetime import datetime, timedelta



class Slownik:
    def __init__(self):
        pogoda = {}


class API():
    def __init__(self):
        self.API_klucz = "4dff31c855f6108ab6652907f07d9060"
        wwa_lat = 52.2319581
        wwa_lon = 21.0067249
        API_URL = F"https://api.openweathermap.org/data/2.5/onecall?lat={wwa_lat}&lon={wwa_lon}&exclude=hourly,minutely,alerts&appid={self.API_klucz}"
        odpowiedz = requests.get(API_URL)
        self.zapytanie = odpowiedz.json()



class WeatherForecast(API):

    def __init__(self, klucz_API):
        super().__init__()
        self.klucz_API =  klucz_API
        self.pogoda = {}
        self.pogoda_historia = {}



    def __iter__(self):
            for x in self.zapytanie["daily"]:
             data_format = datetime.fromtimestamp(x["dt"]).date()
             dzien = str(data_format)
             if not dzien:
              break
             else:
              yield dzien


    def __getitem__(self, podany_dzien):

        if os.stat("weather_history.json").st_size > 0:
            print("Sprawdzam historię...")
            with open("weather_history.json", "r") as plik:
                sprawdzenie_historii = json.load(plik)
                wyszukiwanie = sprawdzenie_historii.get(podany_dzien)
                if wyszukiwanie:
                    print(F"{podany_dzien}: {wyszukiwanie}")
                    exit()
                else:
                    print("Wysyłam zapytanie...")

            for x in self.zapytanie["daily"]:
             data_format = datetime.fromtimestamp(x["dt"]).date()
             dzien = str(data_format)

             # if os.stat("weather_history.json").st_size > 0:
             #     print("Sprawdzam historię...")
             #     with open("weather_history.json", "r") as plik:
             #         sprawdzenie_historii = json.load(plik)
             #         wyszukiwanie = sprawdzenie_historii.get(podany_dzien)
             #         if wyszukiwanie:
             #             print(F"{podany_dzien}: {wyszukiwanie}")
             #             exit()
             #         else:
             #             print("Wysyłam zapytanie...")

             if podany_dzien == dzien:
                 rain = x.get("rain")
                 if rain:
                     self.pogoda_historia[dzien] = ["pada"]
                     return (F"{podany_dzien}: pada")

                 else:
                     self.pogoda_historia[dzien] = ["nie pada"]
                     return (F"{podany_dzien}: nie pada")

            if podany_dzien not in self.pogoda:
                print("Brak informacji dla podanej daty")
                exit()

    def items(self):
        with open("weather_history.json", "r") as plik:

            pogoda_hi = json.load(plik)
            for x,y in pogoda_hi.items():
                yield x,y



wf = WeatherForecast("4dff31c855f6108ab6652907f07d9060")





# for dane in wf:
#     print(dane)

print(wf["2022-06-15"])
#
#
# for data in wf.items():
#     print(data)

