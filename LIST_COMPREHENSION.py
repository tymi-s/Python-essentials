

#list comprehension jest do tworzenia nowej listy na podstawie już istniejącej używając krótszej sładni

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
only_with_a=[]

for x in fruits:
    if "a" in x:
        only_with_a.append(x)
print(fruits)
print(only_with_a)

# teraz z list comprehesion

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
only_with_a2=[x for x in fruits2 if"a" in x]
print(fruits)
print(only_with_a2)



###### tylko mango
tekst=["mango","banana","cherry","mango","mango"]
mango=[]
for x in tekst:
    if x =="mango":
        mango.append(x)

print("\n\n",tekst,"\n",mango)


#list comprehension
tekst2=["mango","banana","cherry","mango","mango"]
mango2=[x for x in tekst2 if x =="mango"]
not_mango = [x for x in tekst2 if x!="mango"]
not_n = [x for x in tekst2 if "n" not in x]
print("\n\n",tekst2,"\n",mango2,"\n",not_mango,"\n",not_n)

#składnia dla list comprehension:
#newlist = [expression for item in iterable if condition == True]

new = [x for x in range(100) if x%3==0]
print(new)

#upper case
colors = ["blue","black"]
upper_collors=[x.upper() for x in colors]
print(upper_collors)
lower_collors_with_u=[x.lower() for x in colors if "u" in x]
print(lower_collors_with_u)

# z elsem:

objects = ["chair","window","lamp","shelf"]
does_have_a =[ "have" if "a" in x else "does not have" for x in objects  ]
print(objects,"\n",does_have_a)





