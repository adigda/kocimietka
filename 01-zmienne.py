imie = "Damian"
Imie = "Piotr"
nazwisko = "Melniczuk"
wiek = 33
x = 1j

print(x)
print(type(x))
print(type(wiek))
print(imie)
print(imie[3:5])
print(3 + 7)
print(3 == 5)
print(imie.lower())
print(imie.count('a'))
print(wiek)

print(imie + ' ' + nazwisko + 'ma' + str(wiek) + 'lata.')

print("{} {} ma {} lata.".format(imie, nazwisko, wiek/2))
print("{1} {0} ma {2} lata".format(imie, nazwisko, wiek))

# Więcej o printach: https://pyformat.info/