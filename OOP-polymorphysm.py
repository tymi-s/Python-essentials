# polymprphysm means many forms
# in Python it refers to methods,functions and opeators with the same name and can be executed for many objects

#POLYMORPHYSM OF A FUNCTION:

# len() function:
#for list it returns a number of elements:
list = ["hi","mom"]
print(len(list))

#for tuples it returns a number of elements :
tu = ("well","well","well")
print(len(tu))

# for dictionary it returns amounts of key:value pairs:

di ={"name":"Fido","age":2}

print(len(di))

#POLYMORPHYSM OF A CLASS:
#allows many classes to have methods with the same name but doing different things:

class car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def ret(self):
        print("CAR BRAND: ",self.brand)
        print("CAR SPEED: ",self.speed)

cars = car("kia",200)


class kids:
    def __init__(self, age,name):
        self.age = age
        self.name = name

    def ret(self):
        print("KID'S AGE: ", self.age)
        print("KID'S NAME: ", self.name)


kidss = kids(2,"david goggins")
# using ret() for object of different classes:
for x in (cars,kidss):
    x.ret()


# if it comes to a child classes . implementing methods with the same name as a methods from parent classes overrides them

