#1.
#variabila= cutiuta in care punem valori care memoreaza date, acestea se pot modifica(ex.varsta)

#2.
#string
animal = 'papagal'

# int
an = 2022

# float
suma = 15.8

# bool
ploua = True

#-------------------
#3.type
print(type (animal))
print(type (an))
print(type(suma))
print(type(ploua))
#-------------------
#4.
print(round(suma))
suma = round(suma)
print(type(suma))
print(suma)
#-------------------
#5.
print('Animalul meu este ' + animal)
print('M-am nascut in ' + str(an))
print('Am primit rest ' + str(suma))
print('Seara asta ploua '+ str(ploua))
#-------------------
#6.
print('Olari')
print('Domnica')
name = 'OlariDomnica'
# print(f'Numele complet are {len(name)} caractere')
print('Numele complet are ' + str(len(name ) )+' caractere')
# ---------------------
#7.
lungimea = input('lungimea') # nr.citit va fi memorat ca string(am verificat cu functia type)
latimea = input('latimea')
arie = int(lungimea)*int(latimea) # nr care este memorat ca string se converteste catre int
print('Aria dreptunghiului este ' + str(arie))
#--------------------------
#8.'Coral is either the stupidest animal or the smartest rock'
p = 'Coral rock is either the stupidest animal or the smartest rock'
# print(p + str(p.count('the')))   # rezultatul afisat este 3, a numarat si cuvantul either, trebuie sa sparg propozitia in cuvinte
result = p.split()
print(result)
print(p+ ' ' + str(result.count('the'))) # numarul rezultat era lipit de cuv.rock, asa ca am pus ' ' pentru a pune spatiu
#------------------------
#10.
print(p.isnumeric()) # rezultatul asteptat este false
#-----------------------------
#Optionale
#1.
text = input('Va rugam introduceti un text de dimensiune impara ')
lungime = len(text)
mijloc = lungime/2
print(text[int(mijloc)]) #pentru a converti un float catre int am folost functia int
#--------------------------
#2.
nume = input('Introduceti un cuvant ')
inversat =nume[::-1] # ::-1 inseamna de la inceput pana la sfarsit in ordinea inversa
# print('papusica '+ nume[::-1])
assert inversat==nume
#------------------
#3.
text = input(' Introduceti cele 2 cuvinte ') # am citit 2 cuvinte
p=text.split() # le-am spart in 2
cuvint1 = p[0] #am afisat primul cuvant
cuvint2 = p[1] #am afisat al doilea cuvint
print(cuvint1) #am printat primul cuvant
print(cuvint2) #am printat al doilea cuvant
#------------------------
#4.
text = input('Introduceti cuvantul ')
prima_litera = text[0]
# print(prima_litera)
cuvant_partial = text[1:-1].replace(prima_litera, prima_litera.upper()) #cuvantul partial a fost afisat pe jumatate corect(fara prima si fara ulltima litera) dar cu literele mari in mijloc
solutie = text[0] + cuvant_partial + text[-1] # am adaugat prima litere din cuvat + cuvantul partial care era corect + ultima litera care nu era afisata
print(solutie)
#---------------------
#5.
u = input('Introduceti user name ')
p = input('Introduceti parola ')
ascuns = '*'* len(p) #am inmultit * cu lungimea cuvantului
print(ascuns)
