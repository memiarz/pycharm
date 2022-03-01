import sys

akcja = input()
historia = []
saldo = 0
magazyn = {}
hist_tmp = []
ilosc_szt = 0

while True:

    if akcja not in ["saldo", "sprzedaz", "zakup"]:
        print("Brak akcji saldo/sprzedaz/zakup! Koniec")
        break

    if akcja == "saldo":
        saldo_zmiana = int(input())
        saldo_koment = input()

        hist_tmp.append(akcja)
        hist_tmp.append(saldo_zmiana)
        hist_tmp.append(saldo_koment)

        saldo += (saldo_zmiana)

        historia.append(hist_tmp)
        hist_tmp = []


    elif akcja == "zakup":
        produkt_zakup = input()
        cena_zakupu = int(input())
        szt_zakup = int(input())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt_zakup)
        hist_tmp.append(cena_zakupu)
        hist_tmp.append(szt_zakup)

        saldo = saldo - (cena_zakupu * szt_zakup)
        if saldo < 0:
            print()
            print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
            print()
            exit()

        historia.append(hist_tmp)
        hist_tmp = []

        if produkt_zakup not in magazyn:
            magazyn[produkt_zakup] = szt_zakup
        else:
            x = magazyn[produkt_zakup]
            ilosc_szt = x + szt_zakup
            magazyn[produkt_zakup] = ilosc_szt


    elif akcja == "sprzedaz":
        produkt_sprzedaz = input()
        cena_sprzedazy = int(input())
        szt_sprzedaz = int(input())


        hist_tmp.append(akcja)
        hist_tmp.append(produkt_sprzedaz)
        hist_tmp.append(cena_sprzedazy)
        hist_tmp.append(szt_sprzedaz)

        saldo = saldo + (cena_sprzedazy * szt_sprzedaz)

        historia.append(hist_tmp)
        hist_tmp = []

        if produkt_sprzedaz not in magazyn:
            print()
            print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
            print()
            exit()
        if produkt_sprzedaz in magazyn:
            x = magazyn[produkt_sprzedaz]
            ilosc_szt = x - szt_sprzedaz
            magazyn[produkt_sprzedaz] = ilosc_szt
            if ilosc_szt == 0:
                del magazyn[produkt_sprzedaz]
            elif ilosc_szt <0:
                print()
                print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
                print()
                exit()


    if akcja == "stop":
        break

    akcja = input()



print()

for element in historia:
    print(element)

print()

print("Saldo:", saldo)

print()

print("Magazyn:", magazyn)


## SYS.ARGV

if sys.argv[1] == "konto":
    print("Konto:", saldo)

if sys.argv[1] == "magazyn":
    produkt1 = sys.argv[2]
    if produkt1 in magazyn:
        print("W magazynie:",produkt1, magazyn[produkt1] )


    # produkt2 = sys.argv[3]
    # print("Magazyn:",magazyn)

if sys.argv[1] == "przeglad":
    przeglad_od = int(sys.argv[2])
    try:
        przeglad_do = int(sys.argv[3])
        print("Przeglad historii:", historia[przeglad_od:przeglad_do])
    except:
        print("Przeglad historii:", historia[przeglad_od])


    # print("Przeglad historii:", historia[przeglad_od:przeglad_do])



if sys.argv[1] == "saldo":
    kwota = int(sys.argv[2])
    komentarz = sys.argv[3]

    hist_tmp.append(sys.argv[1])
    hist_tmp.append(kwota)
    hist_tmp.append(komentarz)

    historia.append(hist_tmp)
    hist_tmp = []

    saldo += kwota



if sys.argv[1] == "zakup":
    produkt_zakup = sys.argv[2]
    cena_zakupu = int(sys.argv[3])
    szt_zakup = int(sys.argv[4])

    hist_tmp.append(sys.argv[1])
    hist_tmp.append(produkt_zakup)
    hist_tmp.append(cena_zakupu)
    hist_tmp.append(szt_zakup)

    historia.append(hist_tmp)
    hist_tmp = []

    saldo = saldo - (cena_zakupu *szt_zakup)
    if saldo < 0:
        print()
        print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
        print()
        exit()

    if produkt_zakup not in magazyn:
        magazyn[produkt_zakup] = szt_zakup
    else:
        x = magazyn[produkt_zakup]
        ilosc_szt = x + szt_zakup
        magazyn[produkt_zakup] = ilosc_szt


if sys.argv[1] == "sprzedaz":
    produkt_sprzedaz = sys.argv[2]
    cena_sprzedazy = int(sys.argv[3])
    szt_sprzedaz = int(sys.argv[4])

    hist_tmp.append(sys.argv[1])
    hist_tmp.append(produkt_sprzedaz)
    hist_tmp.append(cena_sprzedazy)
    hist_tmp.append(szt_sprzedaz)

    historia.append(hist_tmp)
    hist_tmp = []

    if produkt_sprzedaz not in magazyn:
        print()
        print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
        print()
        exit()
    if produkt_sprzedaz in magazyn:
        x = magazyn[produkt_sprzedaz]
        ilosc_szt = x - szt_sprzedaz
        magazyn[produkt_sprzedaz] = ilosc_szt
        if ilosc_szt == 0:
            del magazyn[produkt_sprzedaz]
        elif ilosc_szt < 0:
            print()
            print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
            print()
            exit()






print("Magazyn:", magazyn)
print(historia)
print(saldo)






"""""
przegląd = ma wczytywać dwie wartości
konto =

jeżeli na początku sprzedamy marchewki których nie mamy: żeby zatrzymywało i nie pokazywało salda

jeżeli saldo poniżej 0 to błąd

jeżeli błąd salda lub sprzedaży to przywracanie ich stanu do poprzedniej wartości i kontynuowanie?

działanie bez inputu

ujemna cena

marchewka: -1

poprawić ify i elify?

magazyn jabłko gruszka banan --> jabłko:0 gruszka:0 banan:0

sprawdzić, czy przegląd -1 do minus czegoś tam działa



"""""




# import sys
#
# if sys.argv[1] == "saldo":
#     while True:
#         akcja_klucz = input()
#         if akcja_klucz == "saldo":
#             saldo_int = int(input())
#             saldo_kom = input()
#             print(f"Saldo: {saldo_int}, {saldo_kom}")
#             break
#
# if sys.argv[1] == "zakup":
#     while True:
#         akcja_klucz = input()
#         if akcja_klucz == "zakup":
#             przedmiot_opis = input()
#             przedmiot_cena = int(input())
#             przedmiot_szt = int(input())
#             print(f"{przedmiot_opis}, cena: {przedmiot_cena}, {przedmiot_szt} szt.")
#             break