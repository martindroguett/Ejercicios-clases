# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:58:32 2024

@author: LabCivil6-Pc15
"""
mayor = -1
nombreM = ""
edad = int(input("Ingresa tu edad (-1 para salir):"))
while edad != -1:
    nombre = input("Ingresa tu nombre: ")
    if edad > mayor:
        mayor = edad
        nombreM = nombre
    edad = int(input("Ingresa tu edad:"))
print(f"{nombreM} es mayor")