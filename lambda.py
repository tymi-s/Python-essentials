#lambda in python is a small anonymous function
# it can take any number of arguments, but can have only one expression
# lambda looks like that:
#lambda arguments : expression
# expression is executed and result is returned (for example to a variable)

x = lambda a,b,c: a+b+c
print (x(13,1,1))

# multiplying

result_of_multiplying = lambda a,b: a*b
print(f"{5} times {3} equels {result_of_multiplying(5,3)}")

#when Lambda is OP:

#lambda is mostly used in other functions for example for multiplying certain variable that function takes by unknown number:
def mult(a):
    return lambda b : a*b
doubling = mult(2)
tripleingxd = mult(3)

print()
print(f"doubling 5: {doubling(5)}\ntripleing 5: {tripleingxd(5)}")


# example abouve shows that we have a function that can do many things thanks to lanbda - we can multiply number by any other only with one function
#we dont need to write a separate function for doubleing and tripleing a numer, lambda allows to cover all of it in one func.



