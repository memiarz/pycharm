# cofnięte defy


import sys

sciezka = sys.argv[1]
f = open(sciezka)

linia = f.readline().strip()

akcja = linia
historia = []
hist_tmp = []
saldo = 0
magazyn = {}
ilosc_szt = 0


def dodawanie_historii(argument):
    # f = r"C:\Users\MRC22\PycharmProjects\python-nauka\acc_imp\acc2.txt"
    f = sciezka
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
        else:
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
