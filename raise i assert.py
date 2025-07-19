def dzielenie(x,y):

    if y==0:
        raise ZeroDivisionError("dzielenie przez 0!!!")# raise pozwala wyrzucić własny błąd z komentarzem
    print(x/y)


try:
    dzielenie(1,0)
except ZeroDivisionError:
    print("\n\nDZIELENIE PRZY ZERO!!!")


#assert - zapewnienie - czyli takie polecenie pozwalające sprawdzić czy wynik jest taki jaki oczekiwaliśmy - do tego jest używany zwraca true lub false:


x=5 # przypuśćmy,że 5 to nasz wynik jakiejś operacji który oczekiwaliśmy

assert x!=5, "Y jest równe 5"# jeśli wyszło nam tyle ile oczekiwaliśmy to powinien wyskoczyć assertError


