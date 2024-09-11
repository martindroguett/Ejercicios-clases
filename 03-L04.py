#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:25:23 2024

@author: martindroguett
"""

# Este programa lee desde el teclado dos números : A y B, y después calcula el resultado de sumar A veces el valor B.

a = int ( input (" Ingresa A: "))
b = int ( input (" Ingresa B: "))

s = 0
while a >= 0:
    s = (s + b) * a
    break
print (s)