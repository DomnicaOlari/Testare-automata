# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
# Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
# metodele clasei.
import math


class Cerc:
    # atribuite
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
       return math.pi * self.raza * self.raza


    def diametru(self):
        return self.raza + self.raza

    def circumferinta(self):
        return 2 * self.raza * math.pi

a= Cerc(5, "rosu")
a.descrie_cerc()
print(a.aria())
print(a.diametru())
print(a.circumferinta())

b=Cerc(10, "roz")
b.descrie_cerc()
print(b.aria())
print(b.diametru())
print(b.circumferinta())

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().
#
class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(self.lungime)
        print(self.latime)
        print(self.culoare)

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.latime + self.lungime)

    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare

c=Dreptunghi(5,2, "portocaliu")
c.descrie()
print(c.aria())
print(c.perimetru())
c.schimba_culoarea("negru")
c.descrie()

d=Dreptunghi(5,2, "galben")
d.descrie()
print(d.aria())
print(d.perimetru())
d.schimba_culoarea("albastru")
d.descrie()


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
import self as self


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(self.nume)
        print(self.prenume)
        print(self.salariu)

    def nume_complet(self):
        return self.nume + ' '+  self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu += self.salariu * (procent/100)

e=Angajat("Rusu","Valerica",4000)
print(e.nume_complet())
print(e.salariu_lunar())
print(e.salariu_anual())
e.marire_salariu(10)
print(e.salariu_lunar())

f=Angajat("Boca", "Vasile", 7000)
print(f.nume_complet())
print(f.salariu_lunar())
print(f.salariu_anual())
f.marire_salariu(7)
print(f.salariu_lunar())

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

  # Titularul x are în contul y suma de n lei

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei")


    def debitare_cont(self, suma):
       self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma

c=Cont("ROINGG0007653233", "Domnica Furnica", 500)
c.afisare_sold()
c.debitare_cont(50)
c.afisare_sold()
c.creditare_cont(1000)
c.afisare_sold()

c2=Cont("RO449AAAA1B31007593840000", "Ion Ion", 3000)
c2.afisare_sold()
c2.debitare_cont(400)
c2.afisare_sold()
c2.creditare_cont(100)
c2.afisare_sold()