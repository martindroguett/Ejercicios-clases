#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:20:43 2024

@author: martindroguett
"""

def distancia(x,y):
    resta = y - x
    distancia = resta - 1
    return distancia

total = 0

arch = open('rangos.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    x = distancia(int(partes[0]),int(partes[1]))
    total += x
    linea = arch.readline().strip()
    
print(f'La suma seria {total}')