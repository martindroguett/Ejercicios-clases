#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:10:43 2024

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

primo = esPrimo(num)

if primo == True:
    print(f'El número {num} es primo')
elif primo == False:
    print(f'El número {num} no es primo')


primo_num = 0
i = 0
while num != primo_num:
    primos = esPrimo(i)
    if primos == True:
        primo_num += 1
    i += 1
    
print(f'El primo número {num} es {i-1}')