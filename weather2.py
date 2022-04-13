import json
from datetime import datetime



class WeatherForecast:

    def __init__(self, klucz_API):
        self.klucz_API = klucz_API
        self.pogoda = {}
        self.pogoda_historia = {}

        with open("daily.json", "r") as plik:
            self.pogoda = json.load(plik)

    def __iter__(self):
            for x in self.pogoda["daily"]:
             data_format = datetime.fromtimestamp(x["dt"]).date()
             dzien = str(data_format)
             if not dzien:
              break
             else:
              yield dzien

    def __getitem__(self, podany_dzien):
            for x in self.pogoda["daily"]:
             data_format = datetime.fromtimestamp(x["dt"]).date()
             dzien = str(data_format)
             if podany_dzien == dzien:
                 rain = x.get("rain")
                 if rain:
                     self.pogoda_historia[dzien] = ["pada"]
                     return (F"{podany_dzien}: pada")

                 else:
                     self.pogoda_historia[dzien] = ["nie pada"]
                     return (F"{podany_dzien}: nie pada")

    def items(self):
        with open("weather_history.json", "r") as plik:

            pogoda_hi = json.load(plik)
            for x,y in pogoda_hi.items():
                yield x,y








wf = WeatherForecast(111)


# for dane in wf:
#     print(dane)
#
# print(wf["2022-03-26"])
#
#
for data in wf.items():
    print(data)

# print(wf.items())