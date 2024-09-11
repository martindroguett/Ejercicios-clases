#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:19:27 2024

@author: martindroguett
"""
x = float(input("Ingrese al menos tres números: "))
mayor1 = -1
mayor2 = -1
mayor3 = -1
while x != -1:
    while x > mayor1 and x > mayor2 and x > mayor3:
       mayor2 = mayor1
       mayor1 = x       
    if x < mayor1 and x > mayor2:
        mayor3 = mayor2
        mayor2 = x
    if x < mayor2 and x > mayor3:
        mayor3 = x
    x = float(input("Ingrese al menos tres números: "))
if mayor1 == -1 or mayor2 == -1 or mayor3 == -1:
    print("No se pueden calcular los números mayores")
if mayor1 > -1 and mayor2 > -1 and mayor3 > -1:
    print(f"Los tres números mayores son {mayor1}, {mayor2} y {mayor3} respectivamente.")