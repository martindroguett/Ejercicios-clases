#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:46:33 2024

@author: martindroguett
"""

variable = int(input("Ingrese Edad: "))
edad = variable
cupon = (input("Posee cupón? (SI/NO): ")).strip().upper()
if edad <= 3:
    print("Entrada Gratuita")
elif edad >= 4 and edad <= 12 and cupon == "SI":
    print("Valor entrada: 3000")
elif edad >= 4 and edad <= 12 and cupon == "NO":
    print("Valor entrada: 5000")
elif edad >= 13 and edad <= 64 and cupon == "SI":
    print("Valor entrada: 8000")
elif edad >= 13 and edad <= 64 and cupon == "NO":
    print("Valor entrada: 10000")
elif edad >= 65 and cupon == "SI":
    print("Valor entrada: 5500")
elif edad >= 65 and cupon == "NO":
    print("Valor entrada: 7500")        