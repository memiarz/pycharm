import sys

f = open(sys.argv[1])

linia = f.readline().strip()

akcja = linia
historia = []
hist_tmp = []
saldo = 0
magazyn = {}
ilosc_szt = 0


def dodawanie_historii(argument):   # importowane do pozostałych plików
    # f = r"C:\Users\MRC22\PycharmProjects\python-nauka\acc_imp\acc2.txt"
    f = sys.argv[1]
    with open(f, "a") as plik:
        plik.write(str(argument) + "\n")


# def historia_zakup_sprzedaz():
#     global hist_tmp, produkt, cena, szt
#
#     produkt = f.readline().strip()
#     cena = int(f.readline().strip())
#     szt = int(f.readline().strip())
#
#     hist_tmp.append(akcja)
#     hist_tmp.append(produkt)
#     hist_tmp.append(cena)
#     hist_tmp.append(szt)
#
#     historia.append(hist_tmp)
#     hist_tmp = []


# def zakup_argv():
#     global hist_tmp, produkt, cena, szt, saldo
#
#     produkt = sys.argv[3]
#     cena_zakupu = int(sys.argv[4])
#     szt_zakup = int(sys.argv[5])
#
#     hist_tmp.append(sys.argv[2])
#     dodawanie_historii(sys.argv[2])
#     hist_tmp.append(produkt)
#     dodawanie_historii(produkt)
#     hist_tmp.append(cena_zakupu)
#     dodawanie_historii(cena_zakupu)
#     hist_tmp.append(szt_zakup)
#     dodawanie_historii(szt_zakup)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo = saldo - (cena * szt)

# def sprzedaz_argv():
#     global hist_tmp, produkt, cena, szt, saldo
#
#     produkt = sys.argv[3]
#     cena = int(sys.argv[4])
#     szt = int(sys.argv[5])
#
#     hist_tmp.append(sys.argv[2])
#     dodawanie_historii(sys.argv[2])
#     hist_tmp.append(produkt)
#     dodawanie_historii(produkt)
#     hist_tmp.append(cena)
#     dodawanie_historii(cena)
#     hist_tmp.append(szt)
#     dodawanie_historii(szt)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo = saldo + (cena * szt)


# def zakup_obliczenie_else():
#     global ilosc_szt, magazyn
#     x = magazyn[produkt]
#     ilosc_szt = x + szt
#     magazyn[produkt] = ilosc_szt

# def sprzedaz_obliczenie_if():
#     global ilosc_szt, magazyn
#     x = magazyn[produkt]
#     ilosc_szt = x - szt
#     magazyn[produkt] = ilosc_szt



### HISTORIA

while True:

    if akcja not in ["saldo", "zakup", "sprzedaz"]:
        print()
        print("Brak akcji saldo/sprzedaz/zakup!")
        print("Nieprawidlowy input!")
        print()
        exit()

    if akcja == "saldo":
        saldo_zmiana = int(f.readline().strip())
        saldo_koment = f.readline().strip()

        hist_tmp.append(akcja)
        hist_tmp.append(saldo_zmiana)
        hist_tmp.append(saldo_koment)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo += (saldo_zmiana)

    elif akcja == "zakup":

        produkt = f.readline().strip()
        cena = int(f.readline().strip())
        szt = int(f.readline().strip())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt)
        hist_tmp.append(cena)
        hist_tmp.append(szt)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo = saldo - (cena * szt)

        if saldo < 0:
            print()
            print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
            print()
            exit()

        if produkt not in magazyn:
            magazyn[produkt] = szt

        elif produkt in magazyn:

            x = magazyn[produkt]
            ilosc_szt = x + szt
            magazyn[produkt] = ilosc_szt

    elif akcja == "sprzedaz":
        produkt = f.readline().strip()
        cena = int(f.readline().strip())
        szt = int(f.readline().strip())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt)
        hist_tmp.append(cena)
        hist_tmp.append(szt)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo = saldo + (cena * szt)

        if produkt not in magazyn:
            print()
            print("Błąd!""\nNie ma takiego produktu w magazynie!")
            print()
            exit()
        if produkt in magazyn:
            x = magazyn[produkt]
            ilosc_szt = x - szt
            magazyn[produkt] = ilosc_szt

            if ilosc_szt == 0:
                del magazyn[produkt]

            elif ilosc_szt < 0:
                print()
                print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
                print()
                exit()

    akcja = f.readline().strip()
    if akcja == "":
        f.close()
        break


### SYS.ARGV

def dozwolone_komendy():
    if sys.argv[2] not in ["konto", "magazyn", "przeglad",
                           "saldo", "zakup", "sprzedaz", "historia", "stan"]:  # USUNAC HISTORIĘ
        print()
        print("Niedozwolona akcja!")
        print()
        exit()





# if sys.argv[2] == "magazyn":
#     print(magazyn)


# if sys.argv[2] == "konto":
#     print()
#     print("Konto:", saldo)

# if sys.argv[2] == "magazyn":
#     print()
#     print("Magazyn: ", end="")
#     for produkt in sys.argv[3:]:
#         print(f"{produkt} {magazyn.get(produkt, 0)} szt., ", end="",)

# if sys.argv[2] == "przeglad":
#     przeglad_od = int(sys.argv[3])
#     try:
#         przeglad_do = int(sys.argv[4])
#         print()
#         print("Przeglad historii:", historia[przeglad_od:przeglad_do])
#         print()
#     except:
#         print()
#         print("Przeglad historii:", historia[przeglad_od])
#         print()

# if sys.argv[2] == "saldo":
#     kwota = int(sys.argv[3])
#     komentarz = sys.argv[4]
#
#     hist_tmp.append(sys.argv[2])
#     dodawanie_historii(sys.argv[2])
#     hist_tmp.append(kwota)
#     dodawanie_historii(kwota)
#     hist_tmp.append(komentarz)
#     dodawanie_historii(komentarz)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo += kwota

# if sys.argv[2] == "zakup":
#
#     produkt = sys.argv[3]
#     cena = int(sys.argv[4])
#     szt = int(sys.argv[5])
#
#     hist_tmp.append(sys.argv[2])
#     dodawanie_historii(sys.argv[2])
#     hist_tmp.append(produkt)
#     dodawanie_historii(produkt)
#     hist_tmp.append(cena)
#     dodawanie_historii(cena)
#     hist_tmp.append(szt)
#     dodawanie_historii(szt)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo = saldo - (cena * szt)


    # if saldo < 0:
    #     print()
    #     print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
    #     print()
    #     exit()
    #
    # if produkt not in magazyn:
    #     magazyn[produkt] = szt
    # else:
    #     x = magazyn[produkt]
    #     ilosc_szt = x + szt
    #     magazyn[produkt] = ilosc_szt


# if sys.argv[2] == "sprzedaz":
#
#     produkt = sys.argv[3]
#     cena = int(sys.argv[4])
#     szt = int(sys.argv[5])
#
#     hist_tmp.append(sys.argv[2])
#     dodawanie_historii(sys.argv[2])
#     hist_tmp.append(produkt)
#     dodawanie_historii(produkt)
#     hist_tmp.append(cena)
#     dodawanie_historii(cena)
#     hist_tmp.append(szt)
#     dodawanie_historii(szt)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo = saldo + (cena * szt)
#
#     if produkt not in magazyn:
#         print()
#         print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
#         print()
#         exit()
#     if produkt in magazyn:
#         x = magazyn[produkt]
#         ilosc_szt = x - szt
#         magazyn[produkt] = ilosc_szt
#
#         if ilosc_szt == 0:
#             del magazyn[produkt]
#         elif ilosc_szt < 0:
#             print()
#             print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
#             print()
#             exit()

# print()
# print()
# for element in historia:
#     print(element)
#
# print()
# print("Saldo:", saldo)
# print()
# print("Magazyn:", magazyn)
#








# plik = r"C:\Users\MRC22\PycharmProjects\python-nauka\acc_imp\acc2.txt"
# with open(plik, "a") as plik:
#     plik.write("sprzedaz" + "\n")
#     plik.write("oranzada" + "\n")
#     plik.write("2500" + "\n")
#     plik.write("2" + "\n")



# plik_do_zapisu = "L5_zapis.txt"   #podajemy nazwę pliku jaki chcemy utworzyć
#
# tresc = "Jakiś tekst do zapisu..."
#
# with open(plik_do_zapisu, "w") as plik:     #tworzy nowy plik .txt
#     plik.write(tresc)









# import sys
#
# f = open("acc.txt")
#
# linia = f.readline().strip()
#
# akcja = linia
# historia = []
# hist_tmp = []
# saldo = 0
# magazyn = {}
# ilosc_szt = 0


# def pobieranie_while():
#
#
# while True:
#
#
#     if akcja not in ["saldo", "zakup", "sprzedaz"]:
#         print()
#         print("Brak akcji saldo/sprzedaz/zakup!")
#         print("Nieprawidlowy input!")
#         print()
#         exit()
#
#     if akcja == "saldo":
#         saldo_zmiana = int(f.readline().strip())
#         saldo_koment = f.readline().strip()
#
#         hist_tmp.append(akcja)
#         hist_tmp.append(saldo_zmiana)
#         hist_tmp.append(saldo_koment)
#
#         saldo += (saldo_zmiana)
#
#         historia.append(hist_tmp)
#         hist_tmp = []
#
#
#     elif akcja == "zakup":
#         produkt_zakup = f.readline().strip()
#         cena_zakupu = int(f.readline().strip())
#         szt_zakup = int(f.readline().strip())
#
#         hist_tmp.append(akcja)
#         hist_tmp.append(produkt_zakup)
#         hist_tmp.append(cena_zakupu)
#         hist_tmp.append(szt_zakup)
#
#         saldo = saldo - (cena_zakupu * szt_zakup)
#
#         if saldo < 0:
#             print()
#             print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
#             print()
#             exit()
#
#         historia.append(hist_tmp)
#         hist_tmp = []
#
#         if produkt_zakup not in magazyn:
#             magazyn[produkt_zakup] = szt_zakup
#         else:
#             x = magazyn[produkt_zakup]
#             ilosc_szt = x + szt_zakup
#             magazyn[produkt_zakup] = ilosc_szt
#
#
#     elif akcja == "sprzedaz":
#         produkt_sprzedaz = f.readline().strip()
#         cena_sprzedazy = int(f.readline().strip())
#         szt_sprzedaz = int(f.readline().strip())
#
#
#         hist_tmp.append(akcja)
#         hist_tmp.append(produkt_sprzedaz)
#         hist_tmp.append(cena_sprzedazy)
#         hist_tmp.append(szt_sprzedaz)
#
#         saldo = saldo + (cena_sprzedazy * szt_sprzedaz)
#
#         historia.append(hist_tmp)
#         hist_tmp = []
#
#         if produkt_sprzedaz not in magazyn:
#             print()
#             print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
#             print()
#             exit()
#         if produkt_sprzedaz in magazyn:
#             x = magazyn[produkt_sprzedaz]
#             ilosc_szt = x - szt_sprzedaz
#             magazyn[produkt_sprzedaz] = ilosc_szt
#
#             if ilosc_szt == 0:
#                 del magazyn[produkt_sprzedaz]
#
#             elif ilosc_szt <0:
#                 print()
#                 print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
#                 print()
#                 exit()
#
#     akcja = f.readline().strip()
#     if akcja == "stop":
#         break
#
#






#
# if sys.argv[1] not in ["konto", "magazyn", "przeglad",
#                        "saldo", "zakup", "sprzedaz"]:
#     print()
#     print("Niedozwolona akcja!")
#     print()
#     exit()
#
# if sys.argv[1] == "konto":
#     print()
#     print("Konto:", saldo)
#
# if sys.argv[1] == "magazyn":
#     print()
#     print("Magazyn: ", end="")
#     for produkt in sys.argv[2:]:
#         print(f"{produkt} {magazyn.get(produkt, 0)} szt., ", end="",)
#
# if sys.argv[1] == "przeglad":
#     przeglad_od = int(sys.argv[2])
#     try:
#         przeglad_do = int(sys.argv[3])
#         print()
#         print("Przeglad historii:", historia[przeglad_od:przeglad_do])
#         print()
#     except:
#         print()
#         print("Przeglad historii:", historia[przeglad_od])
#         print()
#
# if sys.argv[1] == "saldo":
#     kwota = int(sys.argv[2])
#     komentarz = sys.argv[3]
#
#     hist_tmp.append(sys.argv[1])
#     hist_tmp.append(kwota)
#     hist_tmp.append(komentarz)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo += kwota
#
# if sys.argv[1] == "zakup":
#     produkt_zakup = sys.argv[2]
#     cena_zakupu = int(sys.argv[3])
#     szt_zakup = int(sys.argv[4])
#
#     hist_tmp.append(sys.argv[1])
#     hist_tmp.append(produkt_zakup)
#     hist_tmp.append(cena_zakupu)
#     hist_tmp.append(szt_zakup)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     saldo = saldo - (cena_zakupu *szt_zakup)
#     if saldo < 0:
#         print()
#         print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
#         print()
#         exit()
#
#     if produkt_zakup not in magazyn:
#         magazyn[produkt_zakup] = szt_zakup
#     else:
#         x = magazyn[produkt_zakup]
#         ilosc_szt = x + szt_zakup
#         magazyn[produkt_zakup] = ilosc_szt
#
# if sys.argv[1] == "sprzedaz":
#     produkt_sprzedaz = sys.argv[2]
#     cena_sprzedazy = int(sys.argv[3])
#     szt_sprzedaz = int(sys.argv[4])
#
#     hist_tmp.append(sys.argv[1])
#     hist_tmp.append(produkt_sprzedaz)
#     hist_tmp.append(cena_sprzedazy)
#     hist_tmp.append(szt_sprzedaz)
#
#     historia.append(hist_tmp)
#     hist_tmp = []
#
#     if produkt_sprzedaz not in magazyn:
#         print()
#         print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
#         print()
#         exit()
#     if produkt_sprzedaz in magazyn:
#         x = magazyn[produkt_sprzedaz]
#         ilosc_szt = x - szt_sprzedaz
#         magazyn[produkt_sprzedaz] = ilosc_szt
#         if ilosc_szt == 0:
#             del magazyn[produkt_sprzedaz]
#         elif ilosc_szt < 0:
#             print()
#             print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
#             print()
#             exit()
#
# print()
# print()
# for element in historia:
#     print(element)
#
# print()
# print("Saldo:", saldo)
# print()
# print("Magazyn:", magazyn)
#










# import sys
#
# if sys.argv[1] == "akcja":
#     path = r"L5.txt"
#     plik = open(path)
#     dane_z_pliku = plik.read()
#     print("Read():", "\n",dane_z_pliku)
#
#     dane_split = dane_z_pliku.split()
#     print("Split: ", dane_split)
#
#     plik.seek(0)
#
#     plik_readlines = plik.readlines()
#     print("Readlines:", plik_readlines)
    #
    # plik_readline = plik.readline()
    # print("Readline:", plik_readline)


# file_path = r"szkola.txt"
# with open(file_path, "r") as plik:
#     dane = plik.read()
#     dane2 = dane.split
#     print(dane)

#
# else:
#     print("nie udało się")


# plik_zapis = "111.txt"
#
# # tresc1 = "Elo, elo 320"
# tresc1 = "zi zi Top"
# tresc2 = "Vito Bambino"
#
# with open(plik_zapis, "a") as elo:
#     elo.write(str(123) + "\n")
#     elo.write(str(456) + "\n")


