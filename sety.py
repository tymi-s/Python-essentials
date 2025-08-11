#sets - unchangable, has no order, cannot be accesed by an index as it is with list or tupple,DOES NOT ALLOW DUPLICATES
#duplicates will be ignored:

set1= {"new","set","new"}
print(set1)
#values 1 and True are considered duplicated in sets:

set2 = {True,False,1,0}
print(set2)

#set's len:

print(len(set2))

set5 = {1}
print(type(set5))

# looping through a set:
set6 = {1,2,3}
print({x for x in set6})


#looking for "banana" in set:
sets = {"apple","cherry","pinaple","banana"}
print("banana" in sets)

# we can add and delete items from set:
sets.add("orange")
print(sets)
# adding set to another set by update() method:
p= {"corn"}
sets.update(p)
print(sets)

# to the set we can also ad tupple, list or dictionary:
newww= {1,2,3}
wsad = ["hello","world"]
tt= (False,)
newww.update(wsad)
newww.update(tt)
print(newww)


#removing
#remove
api = {"o","r","a","n"}
print(api)
api.remove("r")
print(api)

#discard -better option becouse it does not raise an error when removing non existing item:
api.discard("nnnnnnnn")

#pop - deletes last item but set is unordered so we never know which one will be removed:
api.pop()
print(api)
#ther is aslo clear() method and we can also delete whole set by del set
api.clear()
print(api)
del api

#looping sets:

seter = {1,3,5,7,11,13}
for i in seter:
    print(i)

new_set = {x for x in seter if x == 3}
print(new_set)


#methods of joining sets:
#union(), upgrade() - adding two sets together
# intersection() - keeps only the items that are in both sets
#difference - returns the items that are only in first set
#symetric_difference() - keeps all items without duplicates

set1 = {"apple","banana","orange","cherry"}
set2 = {"apple","banana","orange","coconut"}
set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)

set6= set1.symmetric_difference(set2)
print(set6)


#union() method allows to join sets with other datatypes like tupples. result will be a set
# union() can also be writen as "|"
# difference can also be writen as "-"
# intersection can also be writen as "&"
# symetric_difference can also be writen as "^"

set7 = set1 | set2#union
print(set7)

set8 = set1 & set2
print(set8)

set9 = set1 ^ set2
print(set9)

set10 = set1 - set2
print(set10)