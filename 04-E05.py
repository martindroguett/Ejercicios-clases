#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:29:29 2024

@author: martindroguett
"""

x = int(input('Ingrese edad (Para finalizar ingrese "-1"): '))
nombrem = ""
mayor = 0

if x == -1:
    print("No se puede calcular el mayor")
while x != -1:
    if x > mayor:
        mayor = x
        nombrem = str(input("¿Cuál es el nombre?: "))
    x = int(input('Ingrese edad (Para finalizar ingrese "-1"): '))
if nombrem != "":
    print(f"La persona mayor es {nombrem} y tiene {mayor} años")
    