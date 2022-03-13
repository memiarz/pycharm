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
# up trzeba usunąć duplikatky
# nauczyciel2 = {"1a": ["Jezyk Polski", "Jan Dlugosz"]}     ### jest


# uczen = ["Marcin", "1a", ""]
#



import sys

pobierz = input()

klasa_wych = {}
wychowawca = {}

nauczyciel = {}
nauczyciel_klasy = {}
uczniowie_wg_klas = {}

wychowawcy_lista = []
nauczyciele_lista = []

uczniowie_lista = []
uczniowie_klasy_slownik = {}



while True:
    if pobierz == "wychowawca":

        lista_tmp = []
        lista_tmp2 = []
        # lista_tmp.append(pobierz)     # dodaje "wychowawca" do listy, ale chyba nie potrzebne

        pobierz = input()
        wychowawcy_lista.append(pobierz)
        lista_tmp.append(pobierz)
        wych_klucz = pobierz      # pobieranie do drugiego wyszukiwanie ("wychowawca")


        pobierz = input()
        while len(pobierz) == 2:
            klasa_wych[pobierz] = lista_tmp
            lista_tmp2.append(pobierz)

            pobierz = input()

        wychowawca[wych_klucz] = lista_tmp2


    if pobierz == "nauczyciel":

        lista_tmp = []
        lista_tmp2 = []

        pobierz = input()   #imię nauczyciela
        naucz_imie = pobierz
        nauczyciele_lista.append(pobierz)   # dodanie nauczycieli dla sprawdzenia sys.argv
        lista_tmp2.append(naucz_imie)

        pobierz = input()   # przedmiot nauczyciela
        lista_tmp.append(pobierz)
        lista_tmp2.append(pobierz)  #pobieranie przedmiotu nauczyciela
        lista_tmp2.reverse()
        # lista_duplikat = lista_tmp2

        pobierz = input()
        while len(pobierz) == 2:

            if pobierz not in nauczyciel_klasy.keys():
                lista_tmp.append(pobierz)
                nauczyciel_klasy[pobierz] = lista_tmp2

                nauczyciel[naucz_imie] = lista_tmp
                pobierz = input()
                    # co to jest? coś ważnego?

            if pobierz in nauczyciel_klasy.keys():
                duplikat_klucz = nauczyciel_klasy[pobierz]
                lista_duplikat = duplikat_klucz + lista_tmp2

                nauczyciel_klasy[pobierz] = lista_duplikat

                lista_tmp.append(pobierz)
                nauczyciel[naucz_imie] = lista_tmp

                pobierz = input()

# polecenie dict() ?
# elify

    if pobierz == "uczen":
        tmp = []
        uczen_imie = input()
        uczen_klasa = input()
        uczniowie_lista.append(uczen_imie)  #dodanie ucznia do listy wszystkich uczniów (do sys.argv)
        tmp.append(uczen_imie)

        uczniowie_klasy_slownik[uczen_imie] = uczen_klasa

        if uczen_klasa not in uczniowie_wg_klas.keys():
            uczniowie_wg_klas[uczen_klasa] = tmp


        elif uczen_klasa in uczniowie_wg_klas.keys():
            lista_uczniow_w_klasie = uczniowie_wg_klas[uczen_klasa]
            dodanie_do_klasy = lista_uczniow_w_klasie + tmp
            uczniowie_wg_klas[uczen_klasa] = dodanie_do_klasy


        pobierz = input()


        if pobierz == "koniec":
            break




if len(sys.argv[1]) == 2:
    print(F"Wychowawca: ", klasa_wych[sys.argv[1]])
    print("Uczniowie: ", uczniowie_wg_klas[sys.argv[1]])
# else:
    # print("Błąd!")
    # print(uczniowie_wg_klas)

print("Lista wychowawców: ", wychowawcy_lista)
#
#
arg1 = sys.argv[1]
arg2 = sys.argv[2]
# arg3 = sys.argv[3]        # try/except

wpis = ' '.join([arg1, arg2])
#
# wychowawca:

if wpis in wychowawcy_lista:
    for x in wychowawca[wpis]:
        for uczniowie in uczniowie_wg_klas[x]:
            print(uczniowie)



if wpis in nauczyciele_lista:
    ...


# uczeń:
#
if wpis in uczniowie_klasy_slownik.keys():
    ttt = uczniowie_klasy_slownik.get(wpis)
    print(nauczyciel_klasy[ttt])


# print(uczniowie_wg_klas.keys())



# print()
# print(klasa_wych)
# print()
# print(wychowawca)
# print()
# print(nauczyciel)
# print()
# print(nauczyciel_klasy)
# print()
# print()
# print(uczniowie_wg_klas)
# print()
# print(wychowawcy_lista)
# print()
# print(nauczyciele_lista)
# print()
# print(uczniowie_lista)
# print()
# print(uczniowie_klasy_slownik)
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

