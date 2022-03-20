import sys
import acc2

from acc2 import saldo, dozwolone_komendy

dozwolone_komendy()

if sys.argv[2] == "konto":
    print()
    print("Konto:", saldo)
    print()