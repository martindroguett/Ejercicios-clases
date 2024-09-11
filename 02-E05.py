#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:01:56 2024

@author: martindroguett
"""

año = int(input("Ingrese Año a revisar: "))
if(año / 400 == int(año // 400)):
    print("Es bisiesto.")
elif ((año / 4 == (año) // 4) and (año / 100 != int(año / 100))):
    print("Es bisiesto.")
else: 
    print("No es bisiesto.")