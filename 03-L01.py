#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:47:13 2024

@author: martindroguett
"""

s = 0
x = float(input("Ingresa un número: "))
while x != -1:
    s = s + x
    x = float(input("Ingresa un número: "))
print(f"La suma es {s}.")