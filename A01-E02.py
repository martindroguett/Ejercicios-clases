#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:44:50 2024

@author: martindroguett
"""
print("Dime los lados de un triángulo: ")
lado_1 = float(input("Lado 1: "))
lado_2 = float(input("Lado 2: "))
lado_3 = float(input("Lado 3: "))
if (lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1:
    print("Tu triángulo es válido :D")
    if (lado_1 == lado_2 != lado_3) or (lado_2 == lado_3 != lado_1) or (lado_1 == lado_3 != lado_2):
        print("Tu triángulo es isósceles")
    elif (lado_1 == lado_2 == lado_3):
        print("Tu triángulo es equilátero")
    else: print("Tu triángulo es escaleno")
else: print("Tu triángulo no es válido :(")