#krotki prezchowują wiele elementóów w jednej zmiennej, nie da się zmienić elementów krotki, indeksowanie jest takie jak w liście:
#krotka z jednym elementem musi kończyć się przecinkiem

#lista:
listaa=["turtle","rabit","fish"]
#krotka:
tuplee=("turtle","rabit","fish")
print(type(list),"\n",type(tuple))

tuple2=("turtle",)
not_tupple= ("turle")# string bo nie ma przecinka
print(type(tuple),"\n",type(not_tupple))

#dostawanie się do elementów krotek działa tak samo jak z listami:
t=("pink","black","ugly")
print(t[1])
print(t[:2])

#istnieje obejście które pozwala ZMIENIĆ ELEMENTY KROTKI. Można ją zmienić na listę, zmienić listę a następnie zmienić na krotkie:

tupppple=("turtle","rabit","fish")
lis = list(tupppple)
lis =  ["nyg" for x in lis ]
tupppple=tuple(lis)
print(tupppple)

# krotki można dodawać
t1 = ("my",)
t2 = ("nyg",)
t1 +=t2
print(t1)


# rozpakowywanie krotki
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits
print(green)

# przechodzenie pętlami przez krotke działa jak z listami

# łączenie krotek i przemnażanie ich zawartości
tor = ("black",)
tor *= 5
print(tor)

rot = ("and yellow",)
new = tor +rot
print(new)