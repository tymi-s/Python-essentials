#funkje w pythonie wywołuje się tak jak w c++ czyli nazwa_funkcji(argumenty):
print("Mysia jest piękna")

#aby zdefiniować funkcję musimy użyć słówka def (które jest w miejscu zmiennej w c++):

def pierwsza_funkcja(x):
    print(x)
    return x

y =pierwsza_funkcja(500)
print(y)



#argumenty mogą mieć ustaloną wartość domyślną:
# UWAGA DOMYŚLNE WARTOŚCI MUSZĄ BYĆ NA KOŃCU LISTY ARGUMENTÓW!!!
def funkcja(x,y=5):

    print(x+y)
    return x+y

funkcja(5)
funkcja(5,10)
print(funkcja(6,7))# można łatwo wypisać to co zwraca funkcja bez przydzielania jej do zmiennej

#jeśli funkcja nic nie zwraca to wypisanie zwróconej wartości przez tą funkcje wypisze None czyli brak wartości:

def f(x):
    print(x)

z=f(5)
print(z)