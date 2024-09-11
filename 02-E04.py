#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:47:37 2024

@author: martindroguett
"""

print("¿Qué notas tienes?")
Prueba_1 = float(input("Nota Primera Evaluación:"))
dio_resiliencia = str(input("Rendiste prueba de resiliencia? (Si/No):"))
if dio_resiliencia == str("Si"):
    Resiliencia = float(input("Nota Resiliencia:"))
    Prueba_2 = float(input("Nota Segunda Prueba:"))
else: Prueba_2 = float(input("Nota Segunda Prueba:"))
Control_1 = float(input(("Nota Primer Control:")))
Desafio_1 = float(input("Nota Primer Desafío:"))
Control_2 = float(input("Nota Segundo Control:"))
Desafio_2 = float(input("Nota Segundo Desafío:"))
Asistencia = float(input("¿Cuál es tu % de asistencia?:"))

if dio_resiliencia == str("Si") and Prueba_1 < 4 and Resiliencia >= 4:
    Nota_1 = 4
elif dio_resiliencia == str("Si") and Prueba_1 < 4 and Resiliencia < 4 and Prueba_1 > Resiliencia:
    Nota_1 = Prueba_1
elif dio_resiliencia == str("Si") and Prueba_1 < 4 and Resiliencia < 4 and Prueba_1 < Resiliencia:
        Nota_1 = Resiliencia       
elif dio_resiliencia == str("Si") and Prueba_1 >= 4:
    Nota_1 = float((Prueba_1 + Resiliencia) / 2) 
else: Nota_1 = Prueba_1
promedio_pruebas = float(((Nota_1 * 0.45) + (Prueba_2 * 0.55)))
promedio_controles = float((Control_1 + Control_2 + Desafio_1 + Desafio_2) / 4)

if float(promedio_pruebas) >= 4 and float(promedio_controles) >= 4 and Asistencia >= 70:
    nota_final = ((promedio_pruebas * 0.70) + (promedio_controles * 0.30))
    print(f"¡Aprobaste el ramo con un {nota_final}!")
elif Asistencia >= 70 and promedio_pruebas >= 4 and promedio_controles < 4 and promedio_controles >= 3.4:
    Examen = float(input("Nota examen recuperativo:"))
    if Examen >= 4:
        nota_final = ((promedio_pruebas * 0.70) + (4 * 0.30))
        print(f"¡Aprobaste el ramo con un {nota_final}!")
    else: print(f"Reprobaste el ramo con un {nota_final}")
    
elif Asistencia >= 70 and promedio_controles >= 4 and promedio_pruebas < 4 and promedio_pruebas >= 3.4:
    Examen = float(input("Nota examen recuperativo:"))
    if Examen >= 4:
        nota_final = ((promedio_controles * 0.30) + (4 * 0.70))
        print(f"¡Aprobaste el ramo con un {nota_final}!")
    else: print(f"Reprobaste el ramo con un {nota_final}")

else: print(f"Reprobaste el ramo por asistencia ({Asistencia}%)")
