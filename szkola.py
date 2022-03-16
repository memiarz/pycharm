'''''''''
# wszystkie dane wpisujemy z cudzysłowiem #

# nazwa klasy = wychowawca i uczniowie
# wychowawca = uczniowie wychowawcy
# nauczyciel = wychowawcy wszystkich klas, z którym ma zajęcia nauczyciel
# uczen = lekcje ucznia  i nauczyciele prowadzący lekcje
 '''''''''

import sys

file_path = r"szkola.txt"
with open(file_path, "r") as plik:
    wszystko = plik.read().split("\n")

# print(wszystko)
if sys.argv[1] not in wszystko:
    print("Nie znaleziono w bazie")
    # print(wszystko)
    exit()

# file_path = r"szkola.txt"
# with open(file_path, "r") as plik:
#     for linia in plik:
#         wszystko = plik.read()
#         sycko.append(wszystko)


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

        pobierz = input()
        while len(pobierz) == 2:
            if pobierz not in nauczyciel_klasy.keys():
                lista_tmp.append(pobierz)
                nauczyciel_klasy[pobierz] = lista_tmp2
                nauczyciel[naucz_imie] = lista_tmp
                pobierz = input()
            if pobierz in nauczyciel_klasy.keys():
                duplikat_klucz = nauczyciel_klasy[pobierz]
                lista_duplikat = duplikat_klucz + lista_tmp2
                nauczyciel_klasy[pobierz] = lista_duplikat
                lista_tmp.append(pobierz)
                nauczyciel[naucz_imie] = lista_tmp

                pobierz = input()

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

# klasa:
if len(sys.argv[1]) == 2:
    if sys.argv[1] not in klasa_wych.keys():
        print()
        print("Klasa", sys.argv[1], "nie ma wychowawcy")
        print("Uczniowie", sys.argv[1], ": ", uczniowie_wg_klas[sys.argv[1]])
        exit()
    elif sys.argv[1] in uczniowie_klasy_slownik.values():
        print()
        print("Wychowawca", sys.argv[1], ": ", klasa_wych[sys.argv[1]])
        print("Uczniowie", sys.argv[1], ": ", uczniowie_wg_klas[sys.argv[1]])
        exit()

# wychowawca:
if sys.argv[1] in wychowawcy_lista:
    uczniowie_wychowawcy_lst = []
    if sys.argv[1] in wychowawca.keys():
        for x in wychowawca[sys.argv[1]]:
            for uczniowie in uczniowie_wg_klas[x]:
                uczniowie_wychowawcy_lst.append(uczniowie)
        print()
        print("Uczniowie nauczyciela", sys.argv[1], ": ", uczniowie_wychowawcy_lst, end=", ")

# uczeń:
if sys.argv[1] in uczniowie_klasy_slownik.keys():
    ttt = uczniowie_klasy_slownik.get(sys.argv[1])
    print("\nLekcje ucznia", sys.argv[1], "i nauczyciel przedmiotu:", nauczyciel_klasy[ttt])

# nauczyciel:
if sys.argv[1] in nauczyciele_lista:
    klasy_nauczycieli = nauczyciel[sys.argv[1]]
    klasy_nauczycieli.pop(0)
    nauczyciele_lista_lst = []
    for element in klasy_nauczycieli:
        if element in klasa_wych:
            for klasy in klasa_wych[element]:
                nauczyciele_lista_lst.append(klasy)
        elif element not in klasa_wych:
            continue
    nauczyciele2 = set(nauczyciele_lista_lst)    # usuwa duplikaty z listy (w princie kontynuacja: "list")
    print("\nWychowawcy klas z którymi ma lekcje nauczyciel", sys.argv[1], ": ", list(nauczyciele2))







    # if sys.argv[1] not in uczniowie_wg_klas.keys():
    #     print("Nie ma takiej klasy")
    #     exit()


    # for linia in plik:
    #     print(linia.strip())



# file_path = r"szkola.txt"
# plik = open(file_path, "r")
# # plik.seek(0)
# dane_z_pliku = plik.read()
# split = dane_z_pliku.split()
# # print(dane_z_pliku)
#
# if sys.argv[1] not in dane_z_pliku:     #uwaga na nawiasy kwadratowe
#     print("Nie znaleziono w bazie")
#










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

    # for element in klasy_nauczycieli:
    #     if element in klasa_wych:
    #         for klasy in klasa_wych[element]:
    #             print(klasy)
    #     elif element not in klasa_wych:
    #         continue





# else:
#     print("Błąd! Nie znaleziono wyszukiwania!")

    #
    # for element in klasy_nauczycieli:
    #     for klasy in klasa_wych[element]:
    #         print(klasy)
    #
    # for element in nauczyciel[sys.argv[1]]:
    #     for klasy in klasa_wych[element]:
    #         print(klasy)







# print(uczniowie_wg_klas.keys())


#
# print()
# print("Klasa wychwowawcy: ", klasa_wych)
# print()
# print("Wychowawca: ", wychowawca)
# print()
# print("Nauczyciel: ", nauczyciel)
# print()
# print("Nauczyciele klasy :", nauczyciel_klasy)
# print()
# print()
# print("Uczniowie wg klas: ", uczniowie_wg_klas)
# print()
# print("Wychowawcy lista: ", wychowawcy_lista)
# print()
# print("Nauczyciele lista: ", nauczyciele_lista)
# print()
# print("Uczniowie lista: ", uczniowie_lista)
# print()
# print("Uczniowie_klasy_slownik: ", uczniowie_klasy_slownik)
# print("elo, elo, koniec")
#







# # wpis = sys.argv
# #
# if len(sys.argv) > 2:
#     arg1 = sys.argv[1]
#     arg2 = sys.argv[2]
#     # arg3 = sys.argv[3]
#
#
#     wpis = ' '.join([arg1, arg2])
#
#     #wychowawca
#     if wpis in wychowawcy_lista:
#         for x in wychowawca[wpis]:
#             for uczniowie in uczniowie_wg_klas[x]:
#                 print(uczniowie)
#
#     # uczeń:
#
#     if wpis in uczniowie_klasy_slownik.keys():
#         ttt = uczniowie_klasy_slownik.get(wpis)
#         print(nauczyciel_klasy[ttt])
#
#     # Nauczyciel: {'Jan Dlugosz': ['Jezyk Polski', '1a', '1b', '1c'],
#
#     #nauczyciel:
#
#     if wpis in nauczyciele_lista:
#          print(nauczyciel[wpis])
#
#









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

