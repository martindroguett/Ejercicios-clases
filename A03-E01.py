#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:32:47 2024

@author: martindroguett
"""
tiempo_M = -1
tiempo_m = -1
nombre_M = ""
nombre_m = ""
print('Para finalizar ingrese "-1')
tiempo = int(input("Ingrese tiempo (en segundos): "))
if tiempo != -1:
    nombre = str(input("Ingrese nombre de la mascota: "))
while tiempo != -1:
    if tiempo > tiempo_M:
        tiempo_M = tiempo
        nombre_M = nombre
    if tiempo <= tiempo_M and tiempo >= tiempo_m:
        tiempo_m = tiempo
        nombre_m = nombre
    tiempo = int(input("Ingrese tiempo (en segundos): "))
    if tiempo != -1:
        nombre = str(input("Ingrese nombre de la mascota: "))
if tiempo_m == -1 or tiempo_M == -1 or (tiempo_m == tiempo_M and nombre_m == nombre_M):
    print("No se pueden calcular quienes fueron el más rápidos y más lentos.")
elif tiempo_m == tiempo_M and nombre_m != nombre_M:
    print(f"Hay un empate entre {nombre_m} y {nombre_M} con {tiempo_m} segundos!")
else:  
    print(f"La mascota más rapida es {nombre_m} con {tiempo_m} segundos.")
    print(f"La mascota más lenta es {nombre_M} con {tiempo_M} segundos.")