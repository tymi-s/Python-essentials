class Auto: # klasa bez kostruktora domyślnego # klasy zaczynamy od dużej litery !!!
    marka = "Peugeot"
    przebieg = 300500
    ilosc_drzwi = 5
    konie = 165

    def wypisz(self):             # metoda wypisująca parametry obiektu
        print("Marka: ", self.marka)
        print("Przebieg: ", self.przebieg)
        print("Ilość drzwi: ", self.ilosc_drzwi)
        print("Konie: ", self.konie)

samochod = Auto()
samochod.wypisz()
print ("\nMarka samochodu: ",samochod.marka)

samochod2 = Auto()

print("\n\n",samochod2.marka)
samochod2.marka = "Citroen"

print(samochod2.marka)
#############################################################


# klasa z konstruktore mdomyślnym:
print("\n\nKlasa  człowiek z konstruktorem domyślnym:\n")
class Czlowiek:
    def __init__(self,imie="brak",nazwisko="brak",wiek=0,praca = "brak"):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.praca= praca

    def wypisz(self):
        print("Imie: ",self.imie)
        print("Nazwisko: ",self.nazwisko)
        print("Wiek: ",self.wiek)
        print("Praca: ",self.praca)

    def konstruktor(self,imie,nazwisko,wiek,praca):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.praca = praca

Student = Czlowiek()

Student.wypisz()

Student.konstruktor("Tymon","Szyler",21,"korepetytor")
print("\nPo zmianie:\n")
Student.wypisz()























