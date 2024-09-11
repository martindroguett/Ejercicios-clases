#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:19:36 2024

@author: martindroguett
"""

y = ""
x = 0

mayor1 = -1
cliente1 = ""
mayor2 = -1
cliente2 = ""
mayor3 = -1
cliente3 = ""
while y != "fin" and x != -1:
    while x > mayor1 and x > mayor2 and x > mayor3:
       mayor2 = mayor1
       cliente2 = cliente1
       mayor1 = x       
       cliente1 = y
    if x < mayor1 and x > mayor2:
        mayor3 = mayor2
        cliente3 = cliente2
        mayor2 = x
        cliente2 = y
    if x < mayor2 and x > mayor3:
        mayor3 = x
        cliente3 = y
    y = str(input("Ingrese cliente: ")).lower()
    if y == "fin":
        break
    x = float(input("Ingrese monto: "))
if mayor1 == -1 or mayor2 == -1 or mayor3 == -1 or cliente1 == "" or cliente2 == "" or cliente3 == "":
    print("No se pueden calcular los ganadores")
if mayor1 > -1 and mayor2 > -1 and mayor3 > -1:
    print("Los ganadores son: ")
    print(cliente1)
    print(cliente2)
    print(cliente3)