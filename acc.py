akcja = input()
historia = []
saldo = 0
saldo_hist1 = []
saldo_hist2 = []
zakup_hist = []
sprzedaz_hist = []
magazyn = {}
hist_tmp = []


while True:

    if akcja not in ["saldo", "sprzedaz", "zakup"]:
        print("Błąd! Kończę pracę")
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

        akcja = input()
        if akcja == "saldo":
            continue

    elif akcja == "zakup":
        produkt_zakup = input()
        cena_zakupu = int(input())
        szt_zakup = int(input())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt_zakup)
        hist_tmp.append(cena_zakupu)
        hist_tmp.append(szt_zakup)

        saldo = saldo - (cena_zakupu * szt_zakup)

        historia.append(hist_tmp)
        hist_tmp = []

        akcja = input()

        if akcja == "sprzedaz":
            continue

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

        akcja = input()

        if akcja == "sprzedaz":
            continue

    if akcja == "stop":
        break


print()

for element in historia:
    print(element)

print()

print("Saldo:", saldo)

print()












"""""
przegląd = ma wczytywać dwie wartości
konto =

jeżeli saldo poniżej 0 to błąd

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