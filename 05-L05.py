#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:55:32 2024

@author: martindroguett
"""

arch = open('matriz.txt','r',encoding='utf-8')
linea = arch.readline().strip()
suma = 0

for i in range(int(linea)):
    linea = arch.readline().strip()
    partes = linea.split(',')
    
    for j in range(int(partes[0])):
        suma += int(partes[1+j])
        
print(f'El resultado de la suma de todos los valores de la matriz es {suma}')