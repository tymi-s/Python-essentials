# what is a __str__() method
# It defines what should be displayed when we treat object as a string (for example when we want to print an object):



class Fruit:

    def __init__(self,name="unknown",tase="unknown"):
        self.name = name
        self.tase = tase
    def __str__(self):
        return f"THIS fruits name is {self.name} and it tasts {self.tase}"
mango = Fruit("MANGO","shit ")
print(mango.name,mango.tase)
print(mango)
