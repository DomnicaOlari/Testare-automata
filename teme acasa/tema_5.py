# # 1.Funcție care să calculeze și să returneze suma a două numere
# def aduna(x,y):
#     return x+y
#
# s = aduna(10,20)
# print(s)
#


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def estePar(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
#
# print(estePar(2022))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
# def calculeaza_lungime(nume, prenume, nume_mijlociu):
#     return len(nume+prenume+nume_mijlociu)
# l=calculeaza_lungime('Olari', 'Domnica', '')
# print(l)



# 4. Funcție care returnează aria dreptunghiului
# def aria_dreptunghi(L,l):
#     return L*l
# a=aria_dreptunghi(4,2)
# print(a)


5. Funcție care returnează aria cercului
import math


def arie_cerc(raza):
    return math.pi*raza*raza
ar=arie_cerc(3)
print(ar)

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.
# def cauta(x,s):
#     return x in s
# gasit=cauta('p', 'pisica')
# print(gasit)


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# def printeaza_lower_upper(s):
#     nr_lower = 0
#     nr_upper = 0
#     for l in s:
#         if l.isupper():
#             nr_upper += 1
#         else:
#             nr_lower += 1
#     print(nr_upper)
#     print(nr_lower)
#
# printeaza_lower_upper("Domnica")


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def numere_pozitive(lista):
#     lista_pozitive =[ ]
#     for n in lista:
#         if n >0:
#             lista_pozitive.append(n)
#     return lista_pozitive
#
# lista_noua=numere_pozitive([2,5,7,-3,2])
# print(lista_noua)

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
# def comparare (x,y):
#     if x>y:
#      print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif y>x:
#      print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#     else:
#      print('Numerele sunt egale')
#
# comparare(4,3)
# comparare(3,4)
# comparare(5,5)


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
def adauga(n,sn):
    if n in sn:
        print('Nu am adaugat numărul în set.Acesta există deja')
        return False
    else:
        sn.add(n)
        print('Am adaugat numărul nou în set')
        return True


grup = {8,9,6}
adaugat = adauga(5,grup)
print(adaugat)

# adauga(5,{5,8,9,6})

