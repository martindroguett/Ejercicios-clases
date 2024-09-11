#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:47:53 2024

@author: martindroguett
"""
L = int(input("Tamaño del mundo de Juanito: "))
p = int(input("Posición desde donde salta Juanito: "))
q = int(input("Longitud de cada salto: "))
n = int(input("Cantidad de saltos: "))

p = p + (q * n) #Casilla final

if p > L - 1:
    p = p - (L - 1) - 1
else: p = 0
print("Juanito está en la casilla", p)