# funkcja join do łączenia ciągów znaków:

#JOIN
print("/".join(["1","2","3","4","5","6","7","8","9"]))# wywołanie funkcji join na ciągu znaków z argumentem tabeli spowoduje ,że ciąg ten będzie występował pomiędzy -
# - wszystkimi ciągami znaków


#REPLACE
print("Hellow World. World Hellow")
print("Hello World. World Hellow".replace("World","Kupa"))# funkcja replace zastępuje pierwszy argument w tekscie argumentem drugim


x = "to Jest zdanie"


#STARTSWITH
print(x.startswith("to"))# zwraca true lub false w zależności czy ciąg zaczyna się od tego co podamy jako argument funkcji

#ENDSWITH

print(x.endswith("zdanie")) # analogicznie sprawdza czy ciąg koczy się podanym argumentem



print("e" in x) # sprawdza czy znak e występuje w tekscie x


#UPPER

print(x.upper()) # funkcja używa caps locka do całego ciągu znaków

#LOWER
print(x.lower()) # lower zmienia na małe litery cały tekst

print("\nOPERACJE NA LISTACH:\n")

####################################################################################################################################

lista =[2,4,30,100,20,24,50]

#ALL

if all([i % 2==0 for i in lista] ): # all zwraca true albo false
    print("wszystkie liczby w liscie są parzyste")

else:
    print("nie wszystkie liczby w liscie są parzyste")


# ANY

if any([i% 2 ==0 for i in lista]):# sprawdza czy przynajmniej jedna liczba jest pażysta
    print("Przynajmniej jedna liczba jest parzysta")
else:
    print("Przynajmniej jedna liczba nie jest parzysta")


#ENUMERATE
for i in lista: # funkcja ta ponumeruje nam elementy listy
    print(i)

print("\nZ ENUMERATE:\n")
for i in enumerate(lista): # funkcja ta ponumeruje nam elementy listy
    print(i)

print("\nBEZ NAWIASÓW , ROZDZIELENIE KROTKI:2\n")
for i in enumerate(lista): # funkcja ta ponumeruje nam elementy listy
    print(i[0],i[1])

# funkcja enumerate tworzy krotki!