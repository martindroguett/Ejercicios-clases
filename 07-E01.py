#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:39:03 2024

@author: martindroguett
"""

def ventas(tipo, cantidad):
    if tipo == 'CANCHA':
        total = 20000 * cantidad
    elif tipo == 'PLATEA':
        total = 30000 * cantidad
    elif tipo == 'VIP':
        total = 40000 * cantidad
    return total

t = input('Ingrese tipo de entradas: ').upper()
while t != 'CANCHA' and t != 'PLATEA' and t != 'VIP':
    t = input('Reingrese tipo de entradas: ').upper()
c = int(input('Ingrese cantidad de entradas: '))

print(ventas(t,c))