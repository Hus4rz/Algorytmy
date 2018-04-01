# -*- coding: utf-8 -*-

import math

print('Jest to program napisany w Pythonie 3 przez Hus4rza. Służy on do obliczania NWD za pomocą algorytmu Euklidesa. Wpisz dwie liczby, aby kontynuować.')

a = int(input('Wpisz pierwszą liczbę. ' '\n' ))
b = int(input('Wpisz drugą liczbę. ' '\n'))

def Obliczanie(a, b):
	jestSkonczone = False
	oryginalneA = a
	oryginalneB = b
	while jestSkonczone == False:
		if a == b:
			print("Wynik to: " + str(a))
			jestSkonczone = True
		elif a < b:
			b -= a
			print(b)
		else:
			a -= b
			print(a)
	print('Czy zapisać wynik algorytmu do pliku? Napisz "y", żeby zapisać, albo "n", żeby odrzucić.')
	odpowiedz = input()
	if odpowiedz == 'y':
		text = 'Wynikiem algorytmu jest: ' + str(a) + '\n' + 'Dane oryginalne to: ' + str(oryginalneA) + ' ' + str(oryginalneB) + '\n'
		saveFile = open('wynikiEuklidesa.txt', 'a')
		saveFile.write(text)
		saveFile.close()
		print('Zapisano. Plik znajduje się w folderze z tym skryptem.')
	elif odpowiedz == 'n':
		print('Wynik nie zostanie zapisany.')
	else:
		print('Nie zrozumiano, wynik zostanie odrzucony.')

Obliczanie(a, b)