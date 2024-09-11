#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:54:10 2024

@author: martindroguett
"""
import random
secreto = random.randint(1, 100)
intentos = 0 

intento = int(input("Adivina el número del 1 al 100!: "))
while intento != secreto:
    if intento < secreto:
        print("El número secreto es mayor!")
    elif intento > secreto:
        print("El número secreto es menor!")
    intentos += 1
    intento = int(input("Inténtalo otra vez: "))
intentos += 1
print(f"Adivinaste en {intentos} intentos!!")