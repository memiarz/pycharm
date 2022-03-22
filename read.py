import os
import sys
import csv
import json
import pickle       # reader.py <src> <dst> <change1> <change2> ...

wczytaj_csv = sys.argv[1]
# zapisz_jako = sys.argv[2]
# wiersz = sys.argv[3]
# kolumna = sys.argv[4]
# wartosc = sys.argv[5]



#os.path.exists(path)

plik_istnieje = (os.path.isfile(wczytaj_csv))      #sprawdzenie, czy istnieje plik do odczytu
sciezka_istnieje = os.path.dirname(wczytaj_csv)   # bez slasza: c:\users\mrc22\desktop, ze slaszem: ...\desktop\python

if plik_istnieje:
    print("Jest taki plik")
    pass
else:
    try:
        if sciezka_istnieje:
            print()
            print(F"Plik nie istnieje. Zawartość katalogu [{sciezka_istnieje}]:", "\n", os.listdir(sciezka_istnieje))
            print()
    except:
            print("Błędna ścieżka")
            print()
            exit()












#
# else:
#     try:
#         # ostatni_katalog = os.path.basename(wczytaj_csv)
#         ostatni_katalog = os.path.basename(os.path.dirname(wczytaj_csv))
#
#         print(F"Nie ma takiego pliku! Zawartość katalogu [{ostatni_katalog}]", "\n", os.listdir(wczytaj_csv))
#         # print(F"Nie ma takiego pliku! Zawartość katalogu [{ostatni_katalog}]:")
#     except:
#         print("Nie ma takiego pliku i takiej ścieżki")




    #
    # sciezka_check = (os.path.exists(wczytaj_csv))  # sprawdzenie, czy istnieje taka ścieżka
    # if sciezka_check:
    #     print("Ścieżka istnieje, ale nazwa pliku jest nieprawidłowa")
    #     ostatni_katalog = os.path.basename(wczytaj_csv)
    #     print()
    #     print(F"Nie ma takiego pliku!", "Zawartość katalogu [{ostatni_katalog}]: ", "\n", os.listdir(ostatni_katalog))
    #     print(os.listdir(wczytaj_csv))

    # else:
    #     print("Nieprawidłowa ścieżka!")
    #     exit()
    #

# if sciezka_check:
#     print("Ścieżka istnieje")
# else:
#     print("Nieprawidłowa ścieżka!")
#     exit()
#








# if plik_check:
#     print("jest plik")
# else:
#     print("nie ma pliku")




# print(os.path.isdir("folder\\folder2"))

# with open(wczytaj_csv, "r") as plik:
#     for linia in csv.reader(plik):
#         print(linia)
#



# C:\Users\MRC22\PycharmProjects\python-nauka\acc_imp
#C:\Users\MRC22\PycharmProjects\python-nauka\acc_imp\iris.csv

# C:\Users\MRC22\Desktop\Pajton

#python read.py .\acc_imp\iris_tst.csv










# import os
#
# os.path.basename()
# print(os.path.basename("folder2\\folder3\\folder4"))  # zwraca ostatni element z tego co podajemy
# # ## == folder4
#
# os.path.split()
# print(os.path.split("folder2\\folder3\\folder4\\test.txt"))       # zwraca ostatni plik i ścieżkę wcześniejszą
# # # można sobie sprawdzać, czy ścieżka ma na końcu jakiś plik/folder (czy one istnieją)
#
# os.mkdir()
# os.mkdir("folder1")     #tworzy nowy folder w aktualnym katalogu
# ## nie można dać np ("folder2/folder3, folder4), bo program chce stworzyć ostatni,
# # i sprawdza, czy istnieją poprzednie
#
# # żeby to rozwiązać:
#
# os.mkdirs()
# os.makedirs("folder2/folder3/folder4")      # nie zawsze jest to dobre, bo cośtam cośtam
#
# os.path.isdir()
# print(os.path.isdir("folder\\folder2"))    #sprawdzanie czy foldery i ścieżki istnieją: sprawdza nie pliki, tylko katalogi
#
#
#
# import csv
#
# lista = []
#
# with open("L6_iris.csv", "r") as f:
#     reader = csv.reader(f)            # może być też:  for linia in csv.reader(f)
#     for linia in reader:                             # lista.append(linia)
#         lista.append(linia)
#
# lista.append([1, 1, 1, 1, "nowy wiersz"])
# lista[5] = [2,2,2,2, "zmieniony wiersz"]  # zamienia wiersz na pozycji nr 5
# lista[4][3] = "zmieniony element"       # zamienia tylko 3 element w wierszu nr 4
#
# with open("L6_iris2.csv", "w") as f:  # można też użyć append: with open("L6_iris2.csv", "a")
#     writer = csv.writer(f)            # może być też: writer = csv.writer(f)
#     for linia in lista:               #               writer.writerows(lista)
#         writer.writerow(linia)
#         # dodajemy na koniec to co w lista.append i zapisujemy do L6_iris2.csv