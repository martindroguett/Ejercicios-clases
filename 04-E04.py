#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:17:52 2024

@author: martindroguett
"""

x = float(input('Ingrese notas (Para finalizar ingrese "-1": '))
n = 0 #cantidad de inputs
c = 0 #notas mayores a 4
if x == -1:
    print("No se puede realizar el calculo")
while x != -1:
    n += 1
    if x >= 4:
        c += 1
    x = float(input('Ingrese notas (Para finalizar ingrese "-1": '))
if n > 0:
    porcentaje = 100 * (c / n)
    print.round((f"Las notas mayores a 4 equivalen a un {porcentaje} %"),2)