# 1. if else


# 2. x este nr. natural sau nu
# x = input('Va rugam introduceti numarul ')
# x = int(x)
# if x >= 0:
#     print('nr natural')
# else:
#     print('nr nu este natural')

# 3. x este număr pozitiv, negativ sau neutru.
# x = input('Va rugam introduceti numarul ')
# x = int(x)
# if x > 0:
#     print('nr pozitiv')
# elif x == 0:
#     print('nr neutru')
# else:
#     print('nr negativ')

# 4. x este între -2 și 13
# x = int(input('Va rugam introduceti numarul '))
# if x >= -2 and x <= 13:
#     print('da')
# else:
#     print('nu')


# 5. diferența dintre x și y este mai mică de 5
# x = int(input('Va rugam introduceti valoarea lui x '))
# y = int(input('Va rugam introduceti valoarea lui y '))
# if abs(x-y)<5:  # abs = modulo, cand primeste un numar cu - el returneaza acel numar dar cu plus
#     print('da')
# else:
#     print('nu')


# 6. x NU este între 5 și 27 - a se folosi ‘not’
# x= 5 and 27
# # if x>=5 and x <=27
# print(not x>=5 and x<=27)

# 7.x și y (int)
# Verifier și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.
# x=int(input('Introdu numarul '))
# y=int(input('Introdu numarul '))
# if x==y and y==x:
#      print('Numerele sunt egale')
# else:
#      print(max(x,y))

# 8.X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# x = int(input('Introdu latura triunghiului '))
# y = int(input('Introdu latura triunghiului '))
# z = int(input('Introdu latura triunghiului '))
# if x==y and y==z and z==x :
#     print('Triunghiul este echilateral')
# elif (x==y and y==x) or (x==z and z==x)  or (y==z and z==y) :
#     print('Tringhiul este isoscel')
# else:
#     print('Triunghiul este oarecare')
# se mai poare rezolva si asa
# if x==y and y==z and z==x :
#     print('Triunghiul este echilateral')
# elif x!=y and y!=z and z!=x:
#    print('Tringhiul este oarecare')
# else:
#     print('Triunghiul este isoscel')


# 9.o literă de la tastatură, este vocală sau nu
# l=input('Introdu litera ')
# v= ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
# if l in v:
#     print('Vocala ')
# else:
#     print('Nu este vocala')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# aa=9
# bb=8
# cc=7
# dd=6
# ee=4
# x=int(input('Introduceti numarul '))
# if x>=9:
#     print('A')
# elif x==8:
#     print('B')
# elif x==7:
#     print('C')
# elif x==6:
#     print('D')
# elif x>4:
#     print('E')
# else:
#     print('F')
