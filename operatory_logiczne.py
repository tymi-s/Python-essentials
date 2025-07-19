#operatory logiczne to AND , OR , NOT

wiek = 18
hajs =3000


#zagnieżdżenie bez operatorów logicznych:
if wiek >=18:
    if hajs >=30:
        print("MOZNA WEJSC")
else:
    print("NIE MOZNA WEJSC")


#zagnieżdżenie warunków z operacjami logicznymi:

if( wiek >= 18 and hajs >30): # wykożystanie and
    print("MOZNA WEJSC")
else:
    print("NIE MOZNA WEJSC")


wiek,kasa = 140,5

if wiek < 18 or kasa >=30: # wykożystanie or - dzieci mogą za darmo a dorośli muszą zaplacic 30 zł
    print("MOZNA WEJSC")
else:
    print("NIE MOZNA WEJSC")


# operator logiczny NOT neguje warunek , działa tylko dla jednego warunku:

u=5

if(not u ==3 ): # wykożystanie not - odwraca wartość logiczą
    print("nice")

else:
    print("not nice")


#wagi

if(True or False and False): # operator and (tj. mnożenie) jest wykonywany przed operatorem or (tj. dodawanie)
    print("tak")
else:
    print("nie")

#nawiasy zmieniają kolejność wykonywania operacji logicznych:

if((True or False )and False):
    print("tak")
else:
    print("nie")


    ####################### mini program - sprawdzanie wieku przez kasiera przed kupieniem piwa:
    print("\n\n")
    wiek, kasa,procent1,procent2 = 15,20,0,10

    if wiek >= 18 and kasa >=8:
        print("MOZNA KUPIC")
        if(kasa >8):
            print("RESZTA:",kasa - 8)

    elif procent1 == 0 and kasa >= 15 :
        print("MOZNA KUPIC")
        if(kasa >8):
            print("RESZTA:",kasa - 15)
