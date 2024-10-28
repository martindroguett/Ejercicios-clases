#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:31:32 2024

@author: martindroguett
"""

def convertir1(num):
    iteraciones = 0
    while num != 1:
        if (num % 2) == 0:
            num = num/2
            iteraciones += 1
        elif (num % 2) != 0:
            num = (3 * num) + 1
            iteraciones += 1
        
    return iteraciones

n = int(input('Ingrese N: '))

iteraciones = convertir1(n)
print(f'Iteraciones: {iteraciones}')
            