# i = 2
# f = 2.414141
# c = 0.5 + 1j
#
# print(float(i), int(f), c)

# a = 2 > 1
# print(a)
# print()
# print(type(a))

# b = 2.787989 > 3
# print(b)
# print(type(b))

# napis = "Ala ma kota"
# print(type(napis))
# print(napis[0])
# print(type(napis[0]))
# print(napis[-3:-1])
# print(napis[::1])
# print(napis[::2])

# txt = "datatypes"
# print(txt)
# y = int(len(txt) * 0.5)
# print(txt[y-1:y+2])


# s1 = "fullstack"
# s2 = "Python"
# s1_1 = int(len(s1)/2)
# print(s1_1)
# print(s1[:s1_1] +s2 +s1[s1_1:])

# s1 = "America"
# s2 = "Japan"
#
# # x = s1[0] + s2[0]
# # y = s1[-1] + s2[-1]
# # middle_1 = int(len(s1)/2)
# # middle_2 = int(len(s2)/2)
# # center = middle_1 + middle_2
# # print(x + center + y)
# # # print(x +s1[:middle_1] +s2[:middle_2] + y)

# str1 = "Python"
# str2 = str1[::-1]
# print(str2)

# Jan    = ("Jan", "Kowalski", 33)
# Janina = ("Janina", "Nowak", (21, 12, 1978), 'K')
# print(Jan)
# print(Janina)
#
# imie     = Jan[0]
# nazwisko = Jan[1]
# wiek     = Jan[2]
#
# imie, nazwisko, wiek = Jan
# print(imie, nazwisko, wiek)

# lista = [1, 2, 3, 4, -5, 6, -10]
# print(lista)
#
# liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
# print(liczby)

# imiona = ['Ala', 'Zygmunt', "Alojzy", "Bogusława"]
# print(imiona)
# print(type(imiona))

# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# print(lista)
# print(lista[2:6:2])
# print(lista[:4])
# print(lista[-2:])
# print(lista[::-1])

# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# print(lista)
# lista = [2, 3, 5, 7, 9]
# print(lista)
# lista[2:4] = ["pies", "a", "2"]
# print(lista)

# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# lista.append("zebra")
# print(lista)

# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# lista.insert(2, "zebra")
# print(lista)

# uczestnicy = ["Rafal", "Tomek", "Agata", "Michal", "Robert", "Pawel", "Grzegorz", "Wiktor"]
# nowa_lista = sorted(uczestnicy)
# print(nowa_lista)
# print(len(nowa_lista))
# # uczestnicy.sort()
# # print(uczestnicy)
# # print(len(uczestnicy))

#SŁOWNIK

# slownik = {"ala": "kot", "ola": 1 , "python": True}
# print(slownik)

# tel = {'Maja': 500456, 'Jasio': 343455}
# tel['Ola'] = 3024127
# print(tel)
# del tel['Maja']
# print(tel)

# tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
# print(tel)

#ZBIOR

# zbior = {"ala", "kot", 1, 2.89}
# print(zbior)


# zadanie Napisz program, który:
# Będzie prosił użytkownika o podanie dwóch liczb, i
# Wypisze:
# Wynik ich dzielenia,
# Resztę z dzielenia, oraz
# Wynik dzielenia całkowitego

# print("Podaj pierwsza liczbe: ")
# x = float(input())
# print("Podaj druga liczbe: ")
# y = float(input())
# wynik_dzielenia = x / y
# reszta_z_dzielenia = x % y
# wynik_dzielenia_calkowitego = x // y
# print("Wynik dzielenia: " +str(wynik_dzielenia))
# print("Reszta z dzielenia: " +str(reszta_z_dzielenia))
# print("Wynik dzielenia calkowitego: " +str(wynik_dzielenia_calkowitego))


# Ćwiczenie instrukcji if

# Przypisz 8 do zmiennej x i 15 do zmiennej y
# Utwórz 2 instrukcje warunkowe
# Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
# Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
# Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa

# x = 1
# y = 15
#
# if x > 3 or y % 2 == 0:
#     print("Co najmniej jeden za warunkow jest spelniony")
# if x <= 3 and y % 2 != 0:
#     print("Zaden warunek nie jest spelniony")

# x = True
# if not x:
#     print("warunek spełniony")
# else:
#     print("warunek niespełniony")


# kazda_wartosc = "test" and [123]
# print(kazda_wartosc)

# print("test" or 0)

# print([] and "test")

#Przykład – and
# Zwróć True, jeśli oba stwierdzenia są prawdziwe
# x > 3 i x < 10
# Spróbuj!

# x = float(input("Podaj x: "))
# y = x > 3 and x < 10
# print(y)

# x = float(input("Podaj x: "))
# if x > 3 and x < 10:
#     print(True)
# else:
#     print(False)

#Przykład – or
# Zwróć wartość True, jeśli jedno ze stwierdzeń jest prawdziwe
# x > 4 lub x < 3
# Spróbuj!


# x = float(input("Podaj x: "))
# y = x > 4 or x < 3
# print(y)

#Przykład – not
# Odwróć wynik, zwróć False, jeśli wynik jest prawdziwy
# nie ( x > 3 i x < 10 )
# Spróbuj!

# x = float(input("Podaj x: "))
# if not x > 4 or x < 3:
#     print(True)
# else:
#     print(False)

# x = 2
# print(not(x > 3 and x < 10))



# wartosc = 0
# wartosc = "warunek spełniony" if True else "warunek niespełniony"
# # if True: wartosc = "warunek spełniony"
# print(wartosc)

# nice = True
# personality = ("wredny", "miły")[nice]
# print("Kot jest", personality)


#PETLE
# string = 'Python'
# for litera in string:
#    print('litera:', litera)

# warzywa = ['marchew', 'kalafior', 'kapusta']
# for warzywo in warzywa:
#     print('warzywo:', warzywo)

# warzywa = ['marchew', 'kalafior', 'kapusta']
# i = 1
# for warzywo in warzywa:
#     print('warzywo:', i, warzywo)
#     i += 1

# Zadanie
# Utwórz listę zawierającą imiona wszystkich kursantów
# Następnie ją posortuj alfabetycznie, oraz
# Policz ile z osób na liście jest kobietami
# W tym celu możesz sprawdzić czy imię kończy się na „a”
# uczestnicy = ["Rafal", "Tomek", "Agata", "Michal", "Robert", "Pawel", "Grzegorz", "Wiktor", "Wiktoria", "Agnieszka"]
# uczestnicy.sort()
# i = 0
# for kobiety in uczestnicy:
#     if kobiety[-1]  == "a":
#         i=i+1
# print(i)


# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i, end=', ')

# print(range(2, 11, 2))
#
# lista = list(range(2, 11, 2))
# print(lista)

# for i in range(5):
#     print(i)
# else:
#     print("Gotowe!")


# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby)

# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)

# for num in range(1, 20):
#     if not num % 2:  # num % 2 == 0
#         print('Kolejna liczba parzysta:', num)
#         continue
#     print('Kolejna liczba:', num)
#
#
# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')

# Zadanie
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for

# x = int(input("Podaj pierwsza liczbe: "))
# y = int(input("Podaj druga liczbe: "))
#
# if x > y:
#     print("x jest wieksze od y")
#     n = y
# else:
#     print("x jest mniejsze od y")
#     n = x
# print(n)
#
# for z in range(n, 0, -1):
#     if x % z == 0 and y % z == 0:
#         print(x, "i" , y, "dzieli sie przez" ,z)
#         break


name = input("Proszę wpisać swoje imię.")
# Wpisz swoją odpowiedź tutaj.

if len(name) > 0:
    print(name)
else:
    pass