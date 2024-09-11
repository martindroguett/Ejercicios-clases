#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:36:07 2024

@author: martindroguett
"""

x = float(input('Ingrese un número (Para finalizar ingrese un "-1): '))
s = 0 #suma de datos
n = 0 #cantidad de datos
if x == -1:
    print("No se pueden realizar los cálculos.")
else: 
    while x != -1:
        s = s + x
        n += 1
        promedio = s / n
        x = float(input('Ingrese un número (Para finalizar ingrese un "-1): '))
    print(f"La suma de los datos es {s}")
    print(f"Los datos ingresados son {n}")
    print(f"El promedio de los datos es {promedio}")