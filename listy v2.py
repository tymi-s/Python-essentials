lista = [True,6,7,8,True]
lista2 = list(("apple",True,2.6))



print(lista)
print(type(lista))

print(lista2)
print(type(lista2))

lista.remove(True)
print(lista)

#sprawdzenie czy znajduje sie w liscie

list = [1,3,5,7]
if 3 in list:
    print("DABLJU")


print(list[-3:-1])#3,5


#zmiana zakresu liczb:

listttt = [1,1,1,1,1,1,1]
listttt[2:5] = [2,2,2]
print(listttt)

#podanie większej ilości argumentów niż miejsc do wpasowania:

lis = [2,2,2,2]
lis[0:2]=[5,5,5,5,5,5]
print(lis)

########
li = [ 3,3,3,3]
li[0:3] = [1]
print(li)

##INSERT:

new = [5,5,5,5,5]
print(new)
new.insert(1,1)
print(new)
new[1]=2
print(new)

#rozszerzenie listy:

l1 = [1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)








