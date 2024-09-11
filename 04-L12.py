#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:01:30 2024

@author: martindroguett
"""

x = int(input("¿Cuántos datos serán ingresados?: "))
if x == 0:
    print("No se puede calcular si no hay nadie :(")
else: 
    nombre = str(input("Ingrese nombre: "))
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    for x in range (1, x):
            nombre2 = str(input("Ingrese nombre: "))
            edad2 = int(input(f"Ingrese la edad de {nombre2}: "))
            if edad2 > edad:
                edad = edad2
                nombre = nombre2
            
    print(f"la persona mayor es {nombre} con {edad} años")
                