lista = [1,2,3,4,5]
lista1 = ["Tymon","Szyler","Kendrick"]
i=0
while i < len(lista1):
    print(lista1[i],end=" ")
    i+=1
print("\n")


for x in lista: # po in mamy informacje o obiekcie po ktorym iteruje petla for
    print(x,end=" ")

print("\n")
for x in lista1:
    print(x,end=" ")

# wygenerowanie listy od 0-9 przy pomocy funkcji range:

z = list(range(10))
print("\n")
print(z)

print("\n")

#użycie funkcji range do pętli for:

for x in range(10): # określa ile razy pętla ma zostać wykonana w tym przhypadku jest to 10 razy
    print(x,end=" ")


print("\n")

for h in range(1,11): # range z dwoma argumentami określa od jakiej lizcby iterujemy i do jakiej
    print(h,end=" ")


print("\n") 
# funkcja range z trzema argumentami:

for x in range(0,20,3): # trzeci argument określa o ile liczba ma przeskakiwać
    print(x,end=" ")