#wyjątki to try i except:


p=15
q=0

#print(p/q) # wyrzucany jest wyjątek

try:
    print("KUPA")
    print(p/q) # kompilator spróbuje wykonać to co jest zawarte w try. Jeśli kod w try wyrzuci błąd zawarty w except to omijane jest wszystko co jest w try i program przeskakuje do except
    # dzięki try /except błędy są obsługiwane i działanie programu nie jest przerywane przez kompilator :)
    print("koniec")
except ZeroDivisionError: # program nie jest przerywany po
    print ("Nastąpiło dzielenie przez zero")

print("REST")

print("\n\n")

#jeśli w try except dany wyjątek nie nastąpi to instrukcje zawarte w except'cie nie zostaną wykonane!:

x=5
y=10

try:
    print(int(y/x),end=" ")
    print("UDAŁO SIĘ!!")
except ZeroDivisionError:
    print("NIE UDAŁO SIĘ!!!")

print("Reszta kodu :)")

######### przy większej ilości wyjątków które chcemy oblsłużyć używany większej ilości except'ów:

print("\n\n")
k = "string"
i = 1

try:
    print(int(k+i),end=" ")
    print("UDAŁO SIĘ")
    print(i/0)
except TypeError:# nie dopasowanie typów
    print("TYPE ERROR ;)!!!!")
except ZeroDivisionError:
    print("DZIELENIE PRZEZ ZERO!!!")
print("Reszta kodu :)")


print("\n\n")

## lub używając nawiasów i jednego except'a:

z=1
o=0
string = "KKKKK"

try:
    print(string +z)
    print(z/o)
except (ZeroDivisionError,TypeError):
    print("DZIELENIE PRZEZ ZERO I/LUB NIE DOPASOWANIE TYPÓW PRZY DODAWANIU!!!")


print("\n\n")
# wyjtek pustej listy:

list =[0,1]

try:
    print(list[5])
except IndexError:
    print("NIE MA TAKIEGO INDEXU LISTY!!")
except:
    print("wystąpił inny błąd!!!") ##### UWAGA !!! NIE PRECYZUJĄC WYJĄTKU W EXCEPT'CIE OBSŁUGUJEMY WSZYSTKIE INNE WYJĄTKI KTÓRE MOGĄ WYSTĄPIĆ!!!


### jest też nieobowiązkowy blok finally który występuje po excepcie i zajdzie zawsze nie zależnie od tego czy błąd wystąpi czy też nie

e=5
u=1
s = "IMIE"
lkk=[1]
try:
    #print(s+e)
    #print(e/0)
    #print(int(s))
    print(lkk[5])

except (ZeroDivisionError,TypeError):
    print("\n\nDZIELENIE PRZEZ ZERO I/LUB NIEZGODNOŚĆ TYPÓW PRZY DODAWANIU!!!")

except:
    print("\nwystąpił jeszcze inny błąd lub błędy!!")
finally:
    print("\nFINALLLLY - CZYLI WYKONA SIĘ ZAWSZE")


# PODSUMOWUJĄC:
# TRY I EXCEPT SĄ WYMAGANE A FINALLY NIE
# TRY PRÓBUJE WYKONAĆ KONKRETNĄ INSTRUKCJE , JEŚLI SIĘ WYK0NA TO EXCEPT JEST POMIJANY , JEŚLI WYSTĄPI BŁĄD , RESZTA KODU W TRY ZOSTAJE POMINIĘTA I PRZECHODZIMY DO EXCEPTA
#WYKONA SIĘ ALBO EXCEPT ALBO CAŁE TRY - W ZALEŻNOŚCI CZY WYSTĄPI OBSŁUŻONY BŁĄD CZY NIE
# FINALLY WYKONA SIĘ ZAWSZE 