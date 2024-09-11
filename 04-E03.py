#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:15:12 2024

@author: martindroguett
"""
x = int(input('Ingrese números enteros positivos o 0 (Para finalizar ingrese "-1"): '))
s = 0 #suma
n = 0 #cantidad de inputs
if x == -1:
    print("No se puede calcular el promedio")
while x != -1:
    n += 1
    s = s + x
    x = int(input('Ingrese números enteros positivos o 0 (Para finalizar ingrese "-1"): '))
if n > 0:
    promedio = s / n
    print(f"El promedio es {promedio}")
