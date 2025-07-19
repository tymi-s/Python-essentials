# słownik czyli dictionary to kolejny rodzaj kolekcji. Jedną z kolekcji jest tablica.
# różnica między tablicą a słownikiem jest w nawiasach - (tablica -[], słownik = {})
# elementy słownika to pary elementów nazywane kluczem i wartością (tak jak w normalnych słownikach)

slownik = {1:"Monday",2:"Tuesday",3:"Wednesday",7:"Thursday",}# dla klucza 1 jest przypisana wartość string "Monday"

print("\n",slownik[1]) # zostanie wypisany Monday bo w nawiasach podajemy numer klucza a nie numer pary elementów w słowniku
print(slownik)

slownik[5]="Kupa"  #elementy są dodawane na koniec

print("\n",slownik)

slownik[6]=125 # slownik może przechowywać wartości różych typów
print("\n",slownik)

# klucze slowników nie muszą być wartościami liczbowymi ani całowitymi!:

slownik['x']=123.8

print("\n",slownik)

# print(slownik[30]) - nie można wypisywać niezdefiniowanych indeksów slownika!
print("\n")
print(slownik.get(30,"coś tam"))# jeśli indeks jest niezdefiniowany to wypisywane jest to co jest podane jako drugi parametr funkcji get()
print(slownik.get(1,"coś tam"))

# wypisywanie słownika linijka po linijce przy pomocy pętli:

print("\npętla wypisanie kluczy:")

for i in slownik:# lub in slownik.keys()
    print(i)


print("\npętla wypisanie wartości przypisanych do kluczy:")

for i in slownik.values():
    print(i)

# usuwanie elementu ze słownika przy użyciu funkcji pop:

print("\n usówanie")

print(slownik)
print(slownik.pop(1)) # usunięcie elementu i jego wypisanie
print(slownik)
print(slownik.pop('x'))
print(slownik)