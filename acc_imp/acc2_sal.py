import sys
import acc2

from acc2 import hist_tmp, historia, saldo, dodawanie_historii, dozwolone_komendy

dozwolone_komendy()

if sys.argv[2] == "saldo":
    kwota = int(sys.argv[3])
    komentarz = sys.argv[4]

    hist_tmp.append(sys.argv[2])
    dodawanie_historii(sys.argv[2])
    hist_tmp.append(kwota)
    dodawanie_historii(kwota)
    hist_tmp.append(komentarz)
    dodawanie_historii(komentarz)

    historia.append(hist_tmp)
    hist_tmp = []

    saldo += kwota






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
