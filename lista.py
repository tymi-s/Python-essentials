x = 50 #zmienna x
y = "Hello World!" #zmienna y

lista = [1,2,3,x,y]
print(lista)
print(lista[3])

x = 4000
lista[3] = 4000
print(lista[3])

# zmienne string zachowują się jak listy:

z = "Siemano Kolano"

print(z[0])
print(z)
o=0

while o<= 7:
    print(z[o],end=" ") # tekst jest oddzielany spacją a nie nową linijką
    o+=1


# można łączyć ze sobą listy:

l=[1,2,3]
m=[4,5,6]
print("\n\n\n")
print(l + m + [7,8,9])

# można mnożyć listy:
print(l*5)

# aby wypisać długość listy używamy funkcji len():

b = [1,2,3,4,5,"Hi",7]

print(len(b))

# pętla while wykorzystująca listę:

listaa = [1,3,5,7,9,11]
i = 0
while i < len(listaa):
    print("Mysia:", i)
    i+=1

# aby dodać element do listy na jej koniecuzywamy funkcji append():

list = ["a","b","c"]
list.append("d")
print(list)

list.append(["e","f","g"])# dodanie do listy listy utworzonej dynamicznie
print(list)

# aby wypisać element z listy który jest częścią listy wewnątrz listy musimy użyć dwuch nawiasów:

print(list[4][0])
print(list[4][1])
print(list[4][2])

# aby dodać element do listy na konkretne jej miejsce możemy użyć funkcji insert():

lk=[1,2,3,4,5]
k = "j"
print(lk)
lk.insert(2,k)
print(lk)

#mozemy obliczyć ilość wystapien danego znaku w liscie przy pomocy funkcji count()::

liss = [ 1,2,3,4,4,4,5,6,7,4,4,4]
print("Liczba wystapień czwórki: ",liss.count(4))

#funkcja zwracająca indeks danego elementu w liście to funckja index():

u = [ "a","b","c","d","e","f","g"]
print("eznajduje się na pozycji: ",u.index("e"))

#mozna też usunac element z listy przy pomocy funkcji remove():

lo=[1,2,3,4,5]

print(lo)
lo.remove(3)
print(lo)

# mozemy tez wypisac najwiekszy i najmniejszy element z listy przy pomocy funkcji max() i min():

us = [1,-4,-100,69,6800,-1,5]
print(us)
print("min:",min(us))
print("max:",max(us))

#mozemy też posortować liste przy pomocy funkcji sort():

us.sort()
print("Sortowanie",us)

#mozemy tez odwrócić kolejność elementów w liście przy pomocy funkcji reverse():

us.reverse()
print("Odwrócenie:",us)

#aby usunąć elementy z listu używamy funkcji clear():

us.clear()
print("Czyszczenie:",us)


#sortowanie listy ze stringami:

lop=["d","e","b","a","f","c"]
print(lop)
lop.sort()
print(lop)

# SORTOWANIE JEST WYKONYWANE WEDŁUG KOLEJNOŚCI ALFABETYCZNEJ!!!
lop=["logii","ab","ag","bcg","zo","c"]
print(lop)
lop.sort()
print(lop)

    #### PODSUMOWNANIE:
#append() - dodaje element na koniec listy
#insert(index,znak) - dodaje element na wybrane miejsce w liście
#count() - zlicza ile razy wystepuje dany element na liście
#index() - zwraca index danego elementu na liście
#remove() - usuwa element z listy
#min() - zwraca najmniejszy element z listy
#max() - zwraca największy element z listy
#sort() - sortuje listę od najmniejszego elementu do największego (działa tylko na listach z elementami tego samego typu!)
#reverse() - odwraca kolejność elementów na liście
#clear() - usuwa wszystkie elementy z listy



