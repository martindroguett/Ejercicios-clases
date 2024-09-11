#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:36:55 2024

@author: martindroguett
"""

print("Elija dos números para dividir el primero entre el segundo")
uno = float(input("Primer número:"))
dos = float(input("Segundo número:"))
if float(dos) != 0 and (uno / dos) == int(uno / dos):
   print("La división es entera")
elif float(dos) != 0 and(uno/dos) == float(uno / dos):
    print("El resto de la división es:", (uno % dos))
else: print("¡ERROR! La división se indetermina")

if (uno < dos):
     print(uno, "es menor que", dos)
     if(dos / uno) == (dos // uno):
         print(dos, "es múltiplo de", uno)
elif (uno > dos):
    print(uno, "es mayor que", dos)
    if(uno / dos) == (uno // dos):
        print(uno, "es múltiplo de", dos)
else: print("Ambos números son iguales")


