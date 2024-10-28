#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:19:07 2024

@author: martindroguett
"""

def calcular_x(vel,tiempo):
    distancia = vel * tiempo
    return distancia

def calcular_y(vel,acc,tiempo):
    distancia = ((acc * tiempo * tiempo) / 2) + vel * tiempo
    return distancia

velocidad = int(input('Ingrese la velocidad inicial del proyectil (en m/s): '))
tiempo = int(input('Ingrese el tiempo transcurrido (en s): '))

for i in range (0,tiempo + 1):
    x = calcular_x(velocidad,i)
    y = round(calcular_y(velocidad,-4.9,i),2)
    if y >= 0:
        print(f'A los {i} segundos el proyectil se encuentra en x = {x} e y = {y}')
    else: 
        tiempo = velocidad / 4.9
        print(f'El proyectil toca el suelo en x = {x} a los {tiempo} segundos')
        break