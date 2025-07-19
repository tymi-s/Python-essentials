# wycinki to coś co działą zarówno dla tablica jak i dla krotek:



# wycinki pozwalają nam wyświetlić konkretną częśc elementów tablicy/krotki:

krotka = (1,2,4,5,"tymon","fido")
print(krotka)

print(krotka[0:3]) # wypisze elementy krotki od elementu zerowego do 3 (bez 3) czyli 0,1 i 2

krotka2 = krotka[3:5] # 3 i 4
print(krotka2)

# czyli w wycinkach indeks końcowy nie jest brany pod uwagę , aby wziąść ostatni element tablicy/krotki można wyjść poza skalę krotki/tablicy:

krotka3=(1,2,"baby","girl","NOKIA",5)
krotka4 = krotka3[3:6]
print("\n\n",krotka3)
print(krotka4)

# możemy robić wycinki od końca:

krotka5 = (6,5,4,3,2,1,0)# liczymy od tyłu zaczynając tym razem liczenie od -1 a nie od 0 !!!
krotka6 = krotka5[-5:-2]

print("\n",krotka5)
print(krotka6)


# trzecia cyfra określa o ile będziemy skakać w krotce/tablicy
krotka7 = (0,1,2,3,4,5,6,7)
print("\n",krotka7[0:7])
print(krotka7[0:7:2])
print(krotka7[0::2])# drugi pusty  element oznacza że będziemy przechodzić przez całą krotke/tablice
print(krotka7[:3]) # od początku do trzeciego
print(krotka7[3:])# od trzeciego do końca

# możemy to zastosować do otrzymania odróconej tablicy/krotki:

krotka8=(6,5,4,3,2,1,0)
krotka9 =krotka8[::-1] # w taki sposób możemy łatwo odrócić tablicę/ krotkę. -1 oznacza że przechodzimy od końca co jedne element aż do początku krotki/tablicy
print("\n",krotka8)
print(krotka9)