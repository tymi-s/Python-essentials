# wycinki to kolejny rodzaj kolecji zaraz po tablicy i słowniku
#tuple - krotka - wycinek


# do stworzenia krotki używamy nawiasów okrągłych
krotka = (1,2,3,4,5)
# elementy krotki tak jak w tablicy zaczynają się od zerowego indeksu


# krotki mogą mieć wartości różynch typów
krotka2 =(1,"kupa","Tomasz",True,)
print("\n",krotka2)

# różnicza między krotką a tablicą jest taka że nie można modyfikować elementów krotki a tablicy można. Nie da się modyfikować elementów krotki:

krotka3 = (1,2,2,4,6)
#krootak[4]=5 # wypisze błąd
print(krotka3)

# do zliczania liczby wystąpień elementów też używa się funkcji coutn:

print("\nLiczba elementów: ",krotka3.count(2))

# tak samo możemy wypisać idneks elementu w krotce przy pomocy funkcji index:

print("Index liczby 4: ",krotka3.index(4))

# krotka ma mniej dostępnych funkcji ponieważ modyfikacja jej elementów jest niemożliwa
# jest to uproszczona lista

