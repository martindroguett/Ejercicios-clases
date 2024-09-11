#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:50:39 2024

@author: martindroguett
"""

variable = int(input("Ingrese Número: "))
x = 0
for i in range (2, variable):
    if variable % i == 0:
        x = "No es Primo"
if variable == 1:
    print("No es Primo")
elif variable == 2:
        print("Es Primo")
elif x == "No es Primo":
    print (x)
else: print("Es Primo")