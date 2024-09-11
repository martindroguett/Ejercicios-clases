#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:24:21 2024

@author: martindroguett
"""
inicial = int(input("Elija un número inicial: "))
final = int(input("Elija un número final: "))

x = 0
for i in range (inicial + 1, final):
    x = i + x
print (x)

intervalo = int(input("Elija un intervalo: "))
for inicial in range(inicial, final, intervalo):
    print(inicial)