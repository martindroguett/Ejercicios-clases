#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:21:08 2024

@author: martindroguett
"""
total = 0
count = 0
mayor = -1
menor = 999

archivo = open("Numeros.txt", 'r', encoding = 'utf-8')
linea = archivo.readline()

while linea != "":
    numero = int(linea)
    total += numero
    count += 1 
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    linea = archivo.readline()
    

promedio = (total/count)
print(f'La suma de los datos es {total}')
print(f'El promedio de los datos es {promedio}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
