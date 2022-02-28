akcja = input()
historia = []
saldo = 0
saldo_hist1 = []
saldo_hist2 = []
zakup_hist = []
sprzedaz_hist = []
magazyn = {}



while True:
    if akcja == "saldo":
        saldo_zmiana = int(input())
        saldo_koment = input()

        saldo_hist1.append(akcja)
        saldo_hist1.append(saldo_zmiana)
        saldo_hist1.append(saldo_koment)

        saldo += (saldo_zmiana)

        saldo_hist1_tupla = tuple(saldo_hist1)
        historia.append(saldo_hist1_tupla)

        akcja = input()

        if akcja == "saldo":
            saldo_zmiana = int(input())
            saldo_koment = input()

            saldo_hist2.append(akcja)
            saldo_hist2.append(saldo_zmiana)
            saldo_hist2.append(saldo_koment)

            saldo += (saldo_zmiana)

            saldo_hist2_tupla = tuple(saldo_hist2)
            historia.append(saldo_hist2_tupla)


    if akcja == "zakup":
        produkt_zakup = input()
        cena_zakupu = int(input())
        szt_zakup = int(input())

        zakup_hist.append(akcja)
        zakup_hist.append(produkt_zakup)
        zakup_hist.append(cena_zakupu)
        zakup_hist.append(szt_zakup)

        saldo = saldo - (cena_zakupu * szt_zakup)

        zakup_hist_tupla = tuple(zakup_hist)
        historia.append(zakup_hist_tupla)

    if akcja == "sprzedaz":
        produkt_sprzedaz = input()
        cena_sprzedazy = int(input())
        szt_sprzedaz = int(input())

        sprzedaz_hist.append(akcja)
        sprzedaz_hist.append(produkt_sprzedaz)
        sprzedaz_hist.append(cena_sprzedazy)
        sprzedaz_hist.append(szt_sprzedaz)

        saldo = saldo + (cena_sprzedazy * szt_sprzedaz)

        sprzedaz_hist_tupla = tuple(sprzedaz_hist)
        historia.append(sprzedaz_hist_tupla)

    akcja = input()

    if akcja == "stop":
        break


ilosc_produktow =

=


magazyn = {"Produkt": produkt_zakup, "szt.": szt_zakup}

print(historia)
print(saldo)
print(magazyn)









"""""
przegląd = ma wczytywać dwie wartości
konto =



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