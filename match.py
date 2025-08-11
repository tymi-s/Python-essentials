# match is basically a switch case in c++:

first= input("choice1: ")
second= input("choice2: ")

match second:
    case '1' | '2' if first == second:
        print("WWW")
    case _:
        print("other")