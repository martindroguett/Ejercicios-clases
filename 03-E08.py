#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:24:48 2024

@author: martindroguett
"""
asignatura = (input("Seleccione Asignatura: 1.Programación 2. Programación Avanzada: ")).strip()
programacion = 0
programacion_a = 0
while asignatura != "Salir":
    if asignatura == "1":
        consulta = (input("Seleccione opción: 1.Asistencia 2. Promedio: ")).strip()
        if consulta == "1":
            asistida = int(input("Ingrese Clases Asistidas: "))
            no_asistida = int(input("Ingrese Clases No Asistidas: "))
            porcentaje_a = (round((asistida / (asistida + no_asistida)) * 100))
            print(f"Asistencia: {porcentaje_a} %")
        elif consulta == "2":
            nota_1 = float(input("Ingrese Nota (1): "))
            while nota_1 < 1 or nota_1 > 7:
                nota_1 = float(input("Error, Reingrese Nota (1): "))
            nota_2 = float(input("Ingrese Nota (2): "))
            while nota_2 < 1 or nota_2 > 7:
                nota_2 = float(input("Error, Reingrese Nota (2): "))
            nota_3 = float(input("Ingrese Nota (3): "))
            while nota_3 < 1 or nota_3 > 7:
                nota_3 = float(input("Error, Reingrese Nota (3): "))
            promedio = round(float((nota_1 + nota_2 + nota_3) / 3), 2)
            print(f"Promedio: {promedio}")
        programacion += 1
        if consulta == "Salir":
            break       
    elif asignatura == "2":
        consulta = (input("Seleccione opción: 1.Asistencia 2. Promedio: ")).strip()
        if consulta == "1":
            asistida = int(input("Ingrese Clases Asistidas: "))
            no_asistida = int(input("Ingrese Clases No Asistidas: "))
            porcentaje_a = (round((asistida / (asistida + no_asistida)) * 100))
            print(f"Asistencia: {porcentaje_a} %")
        elif consulta == "2":
            nota_1 = float(input("Ingrese Nota (1): "))
            while nota_1 < 1 or nota_1 > 7:
                nota_1 = float(input("Error, Reingrese Nota (1): "))
            nota_2 = float(input("Ingrese Nota (2): "))
            while nota_2 < 1 or nota_2 > 7:
                nota_2 = float(input("Error, Reingrese Nota (2): "))
            nota_3 = float(input("Ingrese Nota (3): "))
            while nota_3 < 1 or nota_3 > 7:
                nota_3 = float(input("Error, Reingrese Nota (3): "))
            promedio = round(float(nota_1 + nota_2 + nota_3) / 3, 2)
            print(f"Promedio: {promedio}")
        programacion_a += 1
        if consulta == "Salir":
            break
    asignatura = (input("Seleccione Asignatura: 1.Programación 2. Programación Avanzada: ")).strip()
print(f"Se consultaron {programacion} estudiante/s de Programación  y {programacion_a} estudiante/s de Programación Avanzada.")