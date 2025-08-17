from random import randint
# in python variables are only available in region where it's defined. It's called scope

#local scope:
# 1 inside function:
def function():
    var=5

# 2 in function inside function - variable in outer func is available for inner func:

def f1():
    var=5

    def f2():
        var=5.5
        print(var)
    f2()

f1()
# global scope - variable created in global region. It's then available everywhere

x=5

#global keywoard - we use it in other than global scope to create a global variable:

def f3():
    global z
    z=randint(1,100)
f3()
print(f"global keywoard: {z}",)


#nonlocal keywoard - if we have nested functions - this keyword makes variable available in outer function:

def f4():
    o=30000
    def f5():
        nonlocal o
        o=5
    f5()
    return o

print(f4())
