from random import randint ## Importujemy funkcję randint z biblioteki random


i =1

while i <= 10:

    print(i,":",randint(1,50)) # losowanie dziesiecu liczb  z zakresu od 1 do 50
    i += 1


#gierka w której użytkownik próbuje trafić tą samą liczbę co komputer:
print("\n\n\n")
print("Witaj w grze zgadywanki!")

j=1
k=5
los = randint(1,50)
gues = -1

while (j<=k):
    guess = int(input("Podaj liczbę jaką zgadujesz z zakresu od 1 do 50:"))

    if(guess<1 or guess>50):
        print("Liczba jest z poza zakresu losowania (1-50)!")
        continue
    if(guess == los):
        print("ZGADEŁEŚ ZA",j,"RAZEM")
        print("Twoja liczba to:",guess,"a liczba komputera to:",los)
        break

    elif guess< los and j != k:
        print("PODPOWIEDZ: spróbuj większej liczby!")
        print("Pozostało prób:",k-j)
        j+=1
        continue

    elif guess> los and j != k:

        print("PODPOWIEDZ: spróbuj mniejszej liczby!")
        print("Pozostało prób:", k - j)
        j += 1
        continue

    else:
        print("\nNiestety nie udało się odgadnąć liczby! Komputer wylosował:",los)
        break

#morał:
# Gdy używamy input to domyślnie typ danych jest ustawiony na string dla tego musimy go przekonwertować na odpowiedni typ danych w tym przypadku na int!
# wyglada to tak: i = int(input("Podaj liczbę:"))