def rekurencja(x):
    x+=1
    if x<5:
        print(x)
        rekurencja(x)


x=0

rekurencja(x)


print("X po rekurencji: ", x)

def funkcja(x):
    return x+x

#moc funkcji możemy przypisać także do zmiennej , wtedy zmienna staje się funkcją:


zmienna =funkcja

print(zmienna(2))


# funkcja zwracająca kwadrat liczby i funkcja zwracająca sześcian liczby przy użyciu funkcji kwadrat:

def kwadrat(x):
    return x*x


def szescian(fun,x):
    return fun(x)*x

print("Szescian:",szescian(kwadrat,2))


def s(x):
    if(x<=1):

        return 1
    else:
     return x*s(x-1)


print("Silnia:",s(6))


def wypisz(imiona,i,j=0):
    if j<i:
        print(imiona[j],end=" ")
        return wypisz(imiona,i,j+1)

imiona = ["Ania","Basia","Kasia","Zosia"]
i = len(imiona)
wypisz(imiona,i)

