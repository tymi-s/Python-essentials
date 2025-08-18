# try- except formula is used to handle an exceptions

try:
    print("hi"-2)
except TypeError:
    print("TypeError occured")

#defining own exceptions:
# finally - block of try-except formula will always be executed regardles whether exception occured or not
x= 1

while x<15:
    print(x)

    try:
        if x==12:
            raise Exception("equels")
    except Exception :
        print("HANDLED!")
    else:
        print("No exception occured")
    finally:
        print("FINISHED")
    x=x+1