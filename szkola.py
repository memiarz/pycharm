'''''''''
# nazwa klasy = wychowawca i uczniowie
# wychowawca = uczniowie wychowawcy
# nauczyciel = wychowawcy wszystkich klas, z którym ma zajęcia nauczyciel
# uczen = lekcje ucznia  i nauczyciele prowadzący lekcje
 '''''''''

### uczeń:

# klasa_wych = {"1a": ["wychowawca", "Krzysztof Baczynski",]} ### jest
# klasa_uczn = {"1a": ["uczen1", "uczen2", "uczen3"]}

### wychowawca:

# wychowawca = {"Krzysztof Baczynski" : ["1a", "3c"], "Jan Brzechwa" : ["1c", "2b"]}  ### jest
# uczniowie wychowawcy

### nauczyciel:

# nauczyciel = {"Jan Dlugosz": ["Jezyk Polski", "1a", "1b"], "Maria Konopnicka": ["Jezyk Polski", "2a", "2b", "2c"]}  ### jest
# nauczyciel2 = {"1a": ["Jezyk Polski", "Jan Dlugosz"]}     ### jest


# uczen = ["Marcin", "1a", ""]
#


import sys

pobierz = input()

klasa_wych = {}
wychowawca = {}

nauczyciel = {}
nauczyciel_klasy = {}


while True:
    if pobierz == "wychowawca":
        print("jestem w wychowawcy")
        lista_tmp = []
        lista_tmp2 = []
        # lista_tmp.append(pobierz)     # dodaje "wychowawca" do listy, ale chyba nie potrzebne

        pobierz = input()
        lista_tmp.append(pobierz)
        wych_klucz = pobierz      # pobieranie do drugiego wyszukiwanie ("wychowawca")


        pobierz = input()
        while len(pobierz) == 2:
            klasa_wych[pobierz] = lista_tmp
            lista_tmp2.append(pobierz)

            pobierz = input()

        wychowawca[wych_klucz] = lista_tmp2



    if pobierz == "nauczyciel":
        print("jestem w nauczycielu")
        lista_tmp = []
        lista_tmp2 = []

        pobierz = input()   #imię nauczyciela
        naucz_imie = pobierz
        lista_tmp2.append(naucz_imie)

        pobierz = input()   # przedmiot nauczyciela
        lista_tmp.append(pobierz)
        lista_tmp2.append(pobierz)  #pobieranie przedmiotu nauczyciela
        lista_tmp2.reverse()

        pobierz = input()
        while len(pobierz) == 2:
            lista_tmp.append(pobierz)
            nauczyciel_klasy[pobierz] = lista_tmp2

            pobierz = input()

        nauczyciel[naucz_imie] = lista_tmp

    if pobierz == "end":
        break



print(klasa_wych)
print(wychowawca)
print(nauczyciel)
print(nauczyciel_klasy)


print("elo, elo, koniec")







#
# wychowawca_input = {"wychowawca": {"Krzysztof Baczynski":["1a", "1b", "2a"], "Jan Brzechwa":["1c", "2b"]}}
# nauczyciel_input = {"nauczyciel": {"Jan Dlugosz": {"Jezyk Polski":["1a", "1b", "1c"]},
#                                 "Maria Konopnicka": {"Jezyk Polski":["2a", "2b", "2c"]},
#                                 "Stanislaw Lem": {"Fizyka": ["2a", "2b", "2c", "2d"]},
#                                 "Henryk Sienkiewicz": {"Historia": ["1a", "1b", "2a", "2b"]}}}
# uczen_input = {"uczen": {"Jan Długosz": "1a", "Aleksander Fredro": "1b", "Witold Gombrowicz": "1b", "Zbigniew Herbert": "1c",
#                       "Hanna Krall": "2a", "Zygmunt Krasinski": "2a", "Jan Andrzej Morsztyn": "2a", "Małgorzata Musierowicz": "2b",
#                       "Cyprian Kamil Norwid": "2b", "Eliza Orzeszkowa": "1a", "Bolesław Prus": "2b", "Juliusz Słowacki": "2c",
#                       "Julian Tuwim": "2c", "Stanisław Wyspiański": "2c"}}
#
#
# # wychowawca = {"wychowawca": ["Krzysztof Baczynski", "1a", "1b", "2a","Jan Brzechwa", "1c", "2b"]}
#
#
#
#

#
# # wersja 2
#
# wychowawca = {"Krzysztof Baczynski" : ["1a", "1b", "2a"], "Jan Brzechwa" : ["1c", "2b"]}
# nauczyciel = {"Jan Dlugosz" : ["Jezyk polski", "1a", "1b", "1c"], "Maria Konopnicka" : ["Jezyk polski", "2a", "2b", "2c"]}
# uczen = ["Jan Brzechwa", "1a", "Jan Dlugosz", "1a"]
#
#
#
#
#
#
#
# # 1) nazwa klasy = wychowawca i uczniowie
#
# klasa = {"1a": {"wychowawca" : "Krzysztof Baczynski", "uczniowie": ["Jan Brzechwa", "Jan Dlugosz", "Eliza Orzeszkowa"]},
#                 "1b": {"wychowawca": "Krzysztof Baczynski", "uczniowie" : ["Aleksander Fredro", "Witold Gombrowicz"]}}
#
#
#
# # # 2) wychowawca = uczniowie wychowawcy
#
# wychowawca = {"Krzysztof Baczynski" : ["1a"], "Jan Brzechwa" : ["1c", "2b"]}
#
# wyszukiwanie = "Krzysztof Baczynski"
#
#
# if wyszukiwanie in wychowawca.keys():
#     igz = wychowawca.get(wyszukiwanie)
#
#     for uczen in igz:
#         for osoba in klasa[uczen]["uczniowie"]:
#             print(osoba)




























# OUT
# nazwa klasy = wychowawca i uczniowie

#
#
# klasa = {"1a": {"wychowawca" : "Krzysztof Baczynski", "uczniowie": ["Jan Brzechwa", "Jan Dlugosz", "Eliza Orzeszkowa"]},
#                 "1b": {"wychowawca": "Krzysztof Baczynski", "uczniowie" : ["Aleksander Fredro", "Witold Gombrowicz"]}}
#
# wyszukiwanie = "1b"
#
# if wyszukiwanie in klasa.keys():
#     print(klasa[wyszukiwanie])


# klasa = {"1a": {"wychowawca" : "Krzysztof Baczynski", "uczniowie": ["Jan Brzechwa", "Jan Dlugosz", "Eliza Orzeszkowa"],
#                 "1b": {"wychowawca": "Krzysztof Baczynski", "uczniowie" : ["Aleksander Fredro", "Witold Gombrowicz"]}







#
#
#
# [(i, colour.index(c))
#  for i, colour in enumerate(colours)
#  if c in colour]
#
#
# szkola = {}
# szkola.update(wychowawca_input)
# szkola.update(nauczyciel_input)
# szkola.update(uczen_input)
#
# wejscie = "Aleksander Fredro"
#
#
#
# if wejscie in uczen_input["uczen"].keys():
#     print("Jest w szkole")
# else:
#     print("Nie ma w szkole")
#
#
# if wejscie in szkola["uczen"].keys():
#     print(uczen_input["uczen"].get(wejscie))
#
#
# if wejscie in szkola["uczen"].keys():
#     elo1 = (uczen_input["uczen"].get(wejscie))
#     # 1b
#     if elo1 in szkola["nauczyciel"]["Jan Dlugosz"]["Jezyk Polski"]:
#         print("jest")
#
#     for elo1 in szkola["nauczyciel"].values():
#         elo2 = elo1
#         print(elo2)
#
#     if elo1 in szkola["nauczyciel"]["Jan Dlugosz"]["Jezyk Polski"]:
#         print("jest")
#
#





# print(nauczyciel_in["nauczyciel"]["Jan Dlugosz"]["Jezyk Polski"])


# {"Jan Brzechwa": ["1c", "2b" ]}
# OUT

# szkola = {klasy:{"1a:["Wychowawca 1","Kamil Baczyński", "Michał Bajor", "Ewa Drzyzga"]},
#     wychowawca: {"Wychowawca 2": ["Ewa", "Roman", "Paweł"]"}}
#     nauczyciel: {"Nauczyciel": []}}
#     uczeń: {"Mickiewicz": }}




#
# z_pliku = input()
# szkola = ["wszystkie dane"]
# wychowawca = {}
# klasy = []
# wychowawca_nazwisko = []
#
# while True:
#     if z_pliku == "wychowawca":
#         wychowawca_nazwisko = "Krzysztof Baczynski"
#         klasy_in = input()
#
#         while len(klasy_in) == 2:
#             klasy.append(klasy_in)
#
#         break
#
#     wychowawca[wychowawca_nazwisko] = klasy
#     print(wychowawca)






# klasy_lst = []     # lub if len == 2
# wychowawcy_lst = []
# nauczyciele_lst = []
# uczniowie_lst = []

#
#
#
# klasy_i_uczniowie = {"1a": {"Kamil Baczyński": "uczen", "Jan Brzechwa": "uczen"}}
#
#
#
#
# #input
#
# class wychowawca:
#     def __init__(self, imie, klasa ):
#         self.imie = imie
#         self.klasa = klasa
#
#
# class nauczyciel:
#     def __init__(self, imie, przedmiot, klasa):
#         self.imie = imie
#         self.przedmiot = przedmiot
#         self.klasa = klasa
#
# class uczen:
#     def __init__(self, imie, klasa):
#         self.imie = imie
#         self.klasa = klasa
#
#
#
# jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
# jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
# jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
# jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
#
# # output
#
# class Klasa:
#     def __init__(self, klasa, wychowawca, uczniowie  ):
#         self.klasa = klasa
#         self.wychowawca = wychowawca
#         self.uczniowie = uczniowie
#
#
# class Wychowawca:
#     def __init__(self, imie, uczniowie_wychowawcy ):
#         self.imie = imie
#         self.uczniowie = uczniowie_wychowawcy
#
# class Uczen:
#     def __init__(self, imie, lekcje, nauczyciele  ):
#         self.klasa = klasa
#         self.wychowawca = wychowawca
#         self.uczniowie = uczniowie
#
#
#
# class Nauczyciel:
#     def __init__(self, klasa, wychowawca, uczniowie  ):
#         self.klasa = klasa
#         self.wychowawca = wychowawca
#         self.uczniowie = uczniowie
#

