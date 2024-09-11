#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:53:25 2024

@author: martindroguett
"""

x = int(input("Ingrese Número: "))
count = 0
suma = 0
i = 0
while x <= 1:
    x = int(input("Debe ser mayor a 1, Reingrese Número: "))
print("Detalle Primos:")

for i in range (2, x + 1):
    for u in range (2, i):
        if i % u == 0:
            break
    else: 
        print(i)
        count += 1
        suma = suma + i
print(f"Contador primos: {count}")
print(f"Suma primos: {suma}")
