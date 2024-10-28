#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:54:57 2024

@author: martindroguett
"""

print('Para finalizar el programa ingrese "-1" en el nombre.')
estudiante = str(input("Ingrese nombre del estudiante: "))
azules = 0
total_notas = 0
while estudiante != "-1":
    nota = round(float(input('Ingrese notas (Para finalizar ingrese "-1"): ')),2)
    if not nota == -1 or (nota <=7 and nota >= 1):
        nota = round(float(input('Esa nota no es válida, reingrese nota (Para finalizar ingrese "-1"): ')),2)
    notas = 0
    suma = 0
    while nota != -1:   
        if nota >= 4:
            azules += 1
        notas += 1
        total_notas += 1
        suma = suma + nota
        nota = round(float(input('Ingrese notas (Para finalizar ingrese "-1"): ')),2)
    promedio = round((suma / notas),2)
    print(f"El promedio de {estudiante} es {promedio}")
    estudiante = str(input("Ingrese nombre del estudiante: "))

porcentaje = round(((azules / total_notas) * 100),0)
print(f"El total de notas azules es de un {porcentaje}%")