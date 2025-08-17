# inheritance allows to inherit all methods and properties from one class to another.



#parent class:

class Fruit:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f"This fruit's name is: {self.name}")
        return self.name

class Mango(Fruit):
    pass

class grape(Fruit):
    def __init__(self,name,age,taste):# adding a constructor to a child class
        Fruit.__init__(self,name,age)# we can also write super() insted of Fruit
        self.taste = taste

        
    def print_taste(self):
        print(self.taste)

new = Mango("Mango",20)
new.print_name()#this object inherited methods and properties from parent's class

# if we will define an init constructor in child class it will be overwritten. It means that creating an object which type is child class
# the new constructor will be used instead of inherited one

grape = grape("grape",2,"sweet")
grape.print_taste()


