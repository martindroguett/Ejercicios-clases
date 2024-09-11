#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:15:50 2024

@author: martindroguett
"""
n = 0
s = 0
x = float(input("Ingresa un número: "))
while x != -1:
    s = s + x
    n += 1
    x = float(input("Ingresa un número: "))
print(f"La suma es {s} y se ingresaron {n} números.")