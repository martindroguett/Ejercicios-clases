#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:01:46 2024

@author: martindroguett
"""

def entre(numero1, numero2, operacion):
    if operacion == 'suma':
        suma = 0
        for i in range (numero1, numero2 + 1):
            suma += i
        return suma
    elif operacion == 'multiplicacion':
        multi = 1
        for i in range (numero1, numero2 + 1):
            multi *= i
        return multi

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
ope = input('Ingrese operación: ').lower()

print(entre(num1,num2,ope))