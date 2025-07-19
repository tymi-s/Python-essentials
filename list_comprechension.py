# list comprehension czyli wyrażenia listowe pozwalają przeprowadzać modyfikacje na całej liście:

lista=list(range(10)) #jest to zdefiniowanie listy zawierającej liczny od 0 do 9
print(lista)


new = [ i *2 for i in lista] # czytamy od tyłu - lista 'new' jest stworzona z listy 'lista' tylko że każdy jej element jest pomnożony przez 2
print("nowa: " ,new)

nowa2 =[i+2 for i in lista[0:4]]
print("nowa2: ",nowa2)



nowa3 = [i +2 for i in lista if i %2 ==0] # dla każdego pażystego elementu z listy 'lista' # UWAGA TU CHODZI O WARTOŚĆ ELEMENTU A NIE O INDEKS!!!!
# najpierw sprawdzany jest warunek if a potem jest iteracja o 2 każdego elementu przy tworzeniu listy "nowa3"
print("nowa3: ",nowa3)











