#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:44:23 2024

@author: martindroguett
"""

def calcular_distancia(vel,tiempo):
    distancia = vel * tiempo
    return distancia

velocidad = int(input('Ingrese la velocidad del móvil (en m/s): '))
tiempo = int(input('Ingrese el tiempo transcurrido (en s): '))

for i in range (0,tiempo + 1):
    distancia = calcular_distancia(velocidad,i)
    print(f'A los {i} segundos el móvil recorre {distancia} metros')