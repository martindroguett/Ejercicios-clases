#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:05:45 2024

@author: martindroguett
"""
menor = 100000
x = int(input('Ingrese números enteros positivos o 0 (Para finalizar ingrese "-1"): '))
if x == -1:
    print("No se puede calcular el número menor")
while x != -1:
    if x < menor:
        menor = x
    x = int(input('Ingrese números enteros positivos o 0 (Para finalizar ingrese "-1"): '))
if menor != 100000: 
    print(f"El número menor es {menor}")