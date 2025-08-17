# iterator is an object that has a coutable number of values
# we can iterate through an iterator. It means that we can go through its values just like looping through a list
# iterators in Python implements two methods:
# __iter__() - returns iterator
# __next__()

#DIFFERENCE BETWEEN ITERABLE AND ITERATOR:
# all things in python are objects. Tuples lists,string etc. are iterable containers from which we can return an iterator:
tupple = ("one","two","three")
iterator = iter(tupple)
print(type(iterator)) # iterator for tupple
print(next(iterator))# iterating through a tuple without loop
print(next(iterator))


#iterating through string:

s = "NICE"

i = iter(s)
print(next(i))

# HOW FOR LOOP WORKS:

for x in s:# crates an iterator object and executes next() function uppon it
    print(x)


# to create object/class as an iterator we have to define __next__() and __iter__() functions in class:

class apple:

        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            self.a +=1
            return self.a

a = apple()
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# controll iteracion:

class banana:

    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < 15:
            self.a += 1
            x= self.a
            return x

        else:
            raise StopIteration

ban = banana()

print("\n")
for x in ban:
    print(type(x))