#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:10:22 2024

@author: martindroguett
"""

x = int(input('Ingrese número: '))

def factorial(x):   
    total = 1
    for i in range (x):
        total *= (x - i)
        
    return (total)
    
total = factorial(x)

print(f'El factorial de {x} es {total}')