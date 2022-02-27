slowo = input()
historia = []
saldo_stan = 0
saldo_hist1 = []
saldo_hist2 = []
zakup_hist = []
sprzedaz_hist = []
magazyn = {}


while True:
    if slowo == "saldo":
        saldo_hist1.append(slowo)
        slowo = int(input())
        saldo_hist1.append(slowo)
        slowo = input()
        saldo_hist1.append(slowo)
        historia.append(saldo_hist1)

        slowo = input()

        if slowo == "saldo":
            saldo_hist2.append(slowo)
            slowo = int(input())
            saldo_hist2.append(slowo)
            slowo = input()
            saldo_hist2.append(slowo)
            historia.append(saldo_hist2)

    if slowo == "zakup":
        zakup_hist.append(slowo)
        slowo = input()
        zakup_hist.append(slowo)
        slowo = int(input())
        zakup_hist.append(slowo)
        slowo = int(input())
        zakup_hist.append(slowo)
        historia.append(zakup_hist)

    if slowo == "sprzedaz":  # nie akceptuje polskich znaków: po zamiania na "sprzedaż" nie wyświetla się
        sprzedaz_hist.append(slowo)
        slowo = input()
        sprzedaz_hist.append(slowo)
        slowo = int(input())
        sprzedaz_hist.append(slowo)
        slowo = int(input())
        sprzedaz_hist.append(slowo)
        historia.append(sprzedaz_hist)

    slowo = input()

    if slowo == "stop":
        break



print(historia)







#
# if input() == "stop":
#     break













"""""
1. get content in.txt | python acc.py saldo 2000 dofinansowanie
-Wczytanie wszystkich akcji po kolei


"""""




# import sys
#
# if sys.argv[1] == "saldo":
#     while True:
#         slowo_klucz = input()
#         if slowo_klucz == "saldo":
#             saldo_int = int(input())
#             saldo_kom = input()
#             print(f"Saldo: {saldo_int}, {saldo_kom}")
#             break
#
# if sys.argv[1] == "zakup":
#     while True:
#         slowo_klucz = input()
#         if slowo_klucz == "zakup":
#             przedmiot_opis = input()
#             przedmiot_cena = int(input())
#             przedmiot_szt = int(input())
#             print(f"{przedmiot_opis}, cena: {przedmiot_cena}, {przedmiot_szt} szt.")
#             break