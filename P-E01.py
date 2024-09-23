# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:25:07 2024
Elaborar un programa que calcule si el alumno aprobó o reprobó sus asignaturas
@author: cata
"""
nombre = input("Ingresa el nombre del estudiante: ")
ramos = int(input("Ingresa cantidad de ramos: "))
for i in range(ramos):
    asig = input("Nombre de la Asignatura: ")
    nota_1 = float(input("Ingrese nota 1: "))
    nota_2 = float(input("Ingrese nota 2: "))
    promedio = round((nota_1 * 0.45) + (nota_2 * 0.55),2)
    print(f'El promedio de {asig} es de: {promedio}')
    if promedio >= 4.0:
        print("Aprobado")
    elif promedio >= 3.4 and promedio <= 3.9:
        print("Recalificación")
    else: 
        print("Reprobado")
    
