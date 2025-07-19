#pętla while:

i = 0
while i < 10:
    print(i)
    i += 1

print("koniec")

#pętla while nieskończona:

x=0
while True :
    print("x: ",x)
    x += 1
    if x> 100: # przerwanie nieskończonej pętli
        break

print("\n\n")
#ta sama pętla while co u góry tylko że innaczej zapisana
y=0
while y <= 100:
    print("y:",y)
    y += 1


#instrukcja continue ponawia pętle od początku pomijając resztę kodu w pętli:
print("\n\n")
z =0

#drukowanie wartości tylko parzystych:

while z <10:
    z +=1
    if z% 2 == 1:
        continue # jeśli liczba jest nieparzysta to nie zostaje ona wypisana a pętla zaczyna się od nowa :)
    print("z:", z )

