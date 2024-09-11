#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:49:38 2024

@author: martindroguett
"""
mayor = -1
x = int(input('Ingrese números enteros positivos o 0 (Para finalizar ingrese "-1"): '))
if x == -1:
    print("No se puede calcular el número mayor")
while x != -1:
    if x > mayor:
        mayor = x
    x = int(input('Ingrese números (Para finalizar ingrese "-1"): '))
if mayor != -1:
    print(f"El número mayor es {mayor}")