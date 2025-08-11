#dictionaries store pairs. Each pair is made of key and it's value:
dict = {"color":"red",
        "brand":"nike",
        "type":"T-shirt",
        "year":2025,
        "color":"blue"
        }
print(dict)
# dictionaries are ordered, changeable and do not allow duplicates
# because of order, we can refer to a dict items via index
#each pair is a one index
#we can print a cerain pair:
print(len(dict))
print(dict["color"])
print(type(dict))


#accesing a pairs:
#via get() method:
x= dict.get("color")
print("x: ",x)
#via curly braces:
y = dict.get("type")
print("y: ",y)

#geting a list of a keys by keys() method:
keys = dict.keys()
print("\n\nkeys: ",keys)

#geting a list of values by values() merthod:
values = dict.values()
print("values: ",values)

#geting all items in dictionary as a tuples in a list:
tupple_in_list = dict.items()
print("tupple_in_list: ",tupple_in_list,"\n\n")


#adding pair to a dictionary:
dict["owner"]="me"
#dictionary gets updated
print("dict after ading",dict)


#checing if certain key is present in dictionary:

dict2={"name":"Mike",
       "surname":"Wazowsky",
       "age":69,

       }
if "age" in dict2:
    print(f"{dict2["name"]} age is {dict2['age']}")

print("hello" if "size" not in dict2 else "hi")


#we can change a value of a certain key in dictionary:

new={"color1":"blue",
     "color2":"red",
     "color3":"green",
     "color4":"purple",
     }
print(new)
new["color3"]="orange"
print(new)

#update() method will update a value of a certain key:
new.update({"color1":"black"})# so we sen a small dict
print(new)

#by update() method we can also add new pair of items:
new.update({"color5":"babyblue"})
print(new)

#removing values from a dictionary:

# pop() method removes a item via specified key name:

new.pop("color4")
print(new)

#popitem() removes last added item fro ma dict:
new.popitem()
print(new)

#clear() empties a dictionary:
new.clear()
print(new)

#del - completely deletes certain dict:
del new
#print(new) no more existis:


#loopiing through dict:
#we can loop through dictionary's keys values or a items:

to_loop={"s1":100,
         "s2":200,
         "s3":300,
         }

for x in to_loop:
    print("keys: ",x)

for xi in to_loop.items():
    print("items: ",xi)
for x in to_loop.values():
    print("values: ",x)



#copying dictionaries:
# to copy a dict we can use copy() method:
diccc = {"item":1}
dic = diccc.copy()
print(type(dic))



#NESTES DICTIONARY:
#dictionay that contains dictionary is called nested dictionary:


nested1 = {
    "tiger":{
    "weight":65,
    "age":21
    },
    "bird":{
        "weight":1.5,
        "age":2
    }
}

#we can also add a dictionary to a dictionary

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family={"child1" : child1,"kid2" : child2,"kid3":child3}
#accesing those items:
print(family["kid2"]["name"])