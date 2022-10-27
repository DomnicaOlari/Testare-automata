# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.

# for i in range(len(mașini)):
#     # print(f" Mașina mea preferată este {i}")
#     print(f'Masina mea preferata este {mașini[i]}')

# ● Fă același lucru cu un for each.
# for masina in mașini:
#     print(f" Mașina mea preferată este {masina}")

# ● Fă același lucru cu un while.
# i = 0
# while i in range(len(mașini)):
#     print('Masina mea preferata este ' + mașini[i])
#     i+=1

# 2. Aceeași listă:# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# # exceptând primul și ultimul.
# # - Printează lista.

# for i in range(len(mașini)):
#     if i >= 1 and i < len(mașini)-1:
#         mașini[i] = mașini[i].upper()
# else:
#     print(mașini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# # Printează ‘am găsit mașina dorită de dvs’
# # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# # Altfel:
# # Printează ‘Am găsit mașina X. Mai căutam‘

# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for masina in mașini:
#     if masina == 'Mercedes':
#         print('Am găsit mașina dorită de dvs')
#         break
#     else:
#         print(f'Am găsit mașina {masina} . Mai căutam')


# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
# for masina in mașini:
#     if masina == 'Trabant' or masina == 'Lăstun':
#         continue
#     print(f'S-ar putea să vă placă mașina {masina}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

# masini_vechi = [ ]
# for i in range(len(mașini)):
#     if mașini[i] =='Lăstun' or mașini[i] == 'Trabant':
#       masini_vechi.append(mașini[i])
#       mașini[i] = 'Tesla'
# print(f'Modele vechi {masini_vechi}')
# print(f'Modele noi {mașini}')



# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
# pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
# buget_client = 15000
# for i in range(len(list(pret_masini.values()))):
#     if list(pret_masini.values())[i] <= buget_client:
#         print(f' Masinile care se incadreaza in acest buget sunt: {list(pret_masini.keys())[i]}')
# print('')
# for model_masina, pret_masina in pret_masini.items():
#     print(f'Masina {model_masina} - pret: {pret_masina} euro.')
# print('')
# for model_masina, pret_masina in pret_masini.items():
#     if pret_masina <= buget_client:
#         print(f'Pentru un buget sub 15000 euro puteți alege masina {model_masina}, costa {pret_masina} euro.')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# i=0
# for numar in numere:
#     if numar == 3:
#         i += 1
# print(f'Cifra 3 apare de {i} ')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# suma = 0
# for numar in numere:
#     suma += numar
# print(f' Suma numerelor {suma}')


# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# maxim = numere[0]
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
# print(f' Cel mai mare numar {maxim}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3. Afișază noua listă.

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(f'Lista initiala: {numere}')
# for i in range(len(numere)):
#    numere[i]*=-1
# print(f'Noua lista {numere}.')

