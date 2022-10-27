# # 1. Declarare si afisare
# nota_muzicala = ['do','re','mi','fa','sol','la','si','do']
# print(nota_muzicala)
#
# #  Inversează ordinea folosind slicing și suprascrie această listă.
# print(nota_muzicala[::-1])
# nota_muzicala = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
# #
# # #  Printează varianta actuală (inversată).

# print(nota_muzicala)
# # # Pe această listă aplică o metodă care bănuiești că face același lucru,adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# inversare = nota_muzicala.reverse()
# print(nota_muzicala)
#
# # #  Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
# print(nota_muzicala)
#
# # 2. De câte ori apare ‘do’?
# print(nota_muzicala.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă

# list_1 = [3, 1, 0, 2]
# list_2 = [6, 5, 4]

# print(list_1+list_2)

# unire_1 = list_1 + list_2
# print(unire_1)

# print([* unire_1])

# print([*list_1,*list_2])

# 4.Sortează și afișază lista generată la exercițiul anterior.
# print(unire_1)
# unire_1.sort()
# print(unire_1)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:Lista este goală. Lista nu este goală.

# if len(unire_1) == 0:
#     print('Lista este goală. ')
# else:
#     print('Lista nu este goală. ')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# unire_1.clear()
# print()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.Acum ar trebui să se afișeze că lista e goală.
# if len(unire_1) == 0:
#     print('Lista este goală. ')
# else:
#     print('Lista nu este goală. ')


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folosește o funcție că să afișezi Elevii (cheile)
# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor.Ex: ‘Ana a luat nota {x}’. Doar nota o vei lua folosindu-te de cheie
# print('Ana a luat nota ' +  str(dict1.get('Ana')))
# print('Gigel a luat nota ' +  str(dict1.get('Gigel')))
# print('Dorel a luat nota ' +  str(dict1.get('Dorel')))

# 10. Dorel a făcut contestație și a primit 6 Modifică nota lui Dorel în 6. Printează nota după modificare
# dict1['Dorel'] = '6'
# print('Dorel a luat nota ' +  str(dict1.get('Dorel')))

# 11. Gigel se transferă din clasă. Căuta o funcție care să îl șteargă. Vine un coleg nou. Adaugă Ionică, cu nota 9. Printează noii elevi
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

# 12. Set. Adaugă în zilele_sapt ‘luni’. Afișeaza zile_sapt
# zile_sapt= {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# print(zile_sapt)
#
# zile_sapt.add('luni')
# after_zile_sapt = zile_sapt
# print(after_zile_sapt)


# 13.Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii
# weekend = {'sâmbăta', 'duminică'}
# print(weekend.issubset(zile_sapt))
# print(zile_sapt.issubset(weekend))

# 14. Afișează diferențele dintre aceste 2 seturi.
# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))
#
# print(zile_sapt-weekend)
# print(weekend-zile_sapt)

# 15. Afișază intersecția elementelor din aceste 2 seturi.
# intersectie = zile_sapt.intersection(weekend)
# print(intersectie)
# intersectie_2 = weekend.intersection(zile_sapt)
# print(intersectie_2)

