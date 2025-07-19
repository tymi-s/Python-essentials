import random #słówko import to to samo co include w C++. PRZY UŻYCIU IMPORTA , IMPORTUJEMY CAŁĄ BIBLIOTEKĘ
from random import randint # przy użyciu from bibliotek import funkcja IMPORTUJEMU KONKRETNĄ FUNCKCJĘ Z BIBLIOTEKI IMPORT
#BIBLIOTEKI TO INNACZEJ MODUŁY!!!   
print(random.randint(1,10),end=" ") #wywołanie funkcji randint gdy zaimportujemy całą bibliotekę
print(randint(1,10)) # wywołanie funkcji randint gdy zaimportujemy konkretną funkcję z biblioteki

from math import pi
from math import e
from math import sqrt
from math import sin
print(pi)
print(e)
print(int(sqrt(144)))
print(sin(pi/6))

from math import cos as cosinus # pozwala to na używanie innej nazwy danej funkcji zaimportowanej z danej biblioteki:

print(cosinus(0))

import math as kupa

print("Cos pi/3: ",int(kupa.cos(pi/3)))