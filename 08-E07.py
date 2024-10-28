#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:08:50 2024

@author: martindroguett
"""

def calcular_distancia(vel,acc,tiempo):
    distancia = ((acc * tiempo * tiempo) / 2) + vel * tiempo
    return distancia

velocidad = int(input('Ingrese la velocidad inicial del móvil (en m/s): '))
aceleracion = int(input('Ingrese la aceleración del móvil (en m/s2): '))
tiempo = int(input('Ingrese el tiempo transcurrido (en s): '))

for i in range (0,tiempo + 1):
    distancia = calcular_distancia(velocidad,aceleracion,i)
    print(f'A los {i} segundos el móvil recorre {distancia} metros')