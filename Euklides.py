#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

print('Jest to program napisany w Pythonie 3 przez Hus4rza. Służy on do obliczania NWD za pomocą algorytmu Euklidesa. Wpisz dwie liczby, aby kontynuować.')

a = input('Wpisz pierwszą liczbę. ' '\n' )
b = input('Wpisz drugą liczbę. ' '\n')

def Obliczanie(a, b):
	jestSkonczone = False
	while jestSkonczone == False:
		if a == b:
			print("Wynik to: " + str(a))
			jestSkonczone = True
		elif a < b:
			b = b - a
			print(b)
		else:
			a = a - b
			print(a)

Obliczanie(a, b)