#open to funkja do otwierania i tworzenia plików:

plik = open("pliczek.txt", "w") # w jaki write czyli plik do zapisu i tworzy też ten plik
plik1 = open("plik1.txt", "w")
# plik utworzył się w tym samym folderze w którym jest ten kod

print(plik.writable()) # funkcja ta sprawdza czy dany plik jest plikiem zdolnym do odczyta. Wyświetla Bool'a
print(plik1.readable())


# zapisywanie do pliku:

if plik.writable():
    plik.write("SIGMA  ") # na sztywno
    plik1.write(input("Podaj tekst do zapisu do pliku:") + " ")


plik.close()
plik1.close() # zwalnianie pamięci


plik2 = open("plik1.txt", "r") # do odczytu i zapisu


if plik2.readable():
    tekst = plik2.read()

    print(tekst)

# writing zapisuje tekst do pliku nadpisując to co już w nim było , aby zapisać bez usuwania zawartości pliku to należy użyća od append:


plik3 = open("new.txt", "a")

if plik3.writable():
    plik3.write(input("Podaj tekst:") + "\n")


plik3.close()

plik4 = open("new.txt", "r")

if plik4.readable():
    t = plik4.read()
    print(t)



# są też inne sposoby odczytu danych z plików:


plik5 = open("new.txt", "r")

if plik5.readable():
    t = plik5.readlines() # readlines tworzy liste z zawartości pliku:
    print("readlines:")
    print(t)

# listę tą można nastepnie wyświetlić:
print("\nWYŚWIETLENIE LISTY:\n")
for i in t:
    print(i)

# kolejny sposób na wyświtlenie zawartości pliku bezpośrednio przy pomocy pętli:

plik6 = open("new.txt", "r")

if plik6.readable():


    print("\nWYSWIETLENIE ZAWARTOSCI PLIKU PRZY POMOCY PETLI FOR:\n")
    for i in plik6:
        print(i)

