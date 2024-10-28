#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:13:28 2024

@author: martindroguett
"""

def esPrimo (numero):
    primo = True
    div = 0
    if numero <= 1:
        primo = False
        return primo
    for i in range (2, numero):
        if (numero % i ) == 0:
            div += 1
    if div > 0:
        primo = False
        return primo
    else: 
        return primo
num = int(input('Ingrese número: '))

print(esPrimo(num))