#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:24:24 2024

@author: martindroguett
"""
arch = open('matriz.txt','r',encoding='utf-8')
linea = arch.readline().strip()
partes_la = linea.split(',')
ceros = 0
hola = -1

for i in range(int(partes_la[0])):
    linea = arch.readline().strip()
    partes_num = linea.split(',')
    for j in range(0,int(partes_la[1])):
        j = j*3
        suma = 0
        suma = int(partes_num[j]) + int(partes_num[j+1]) + int(partes_num[j+2])
        if suma == 0:
            ceros += 1

print(f'En la matriz hay {ceros} tripletes que suman 0')

