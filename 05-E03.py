#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:05:13 2024

@author: martindroguett
"""
arch = open('Sucursales.txt','r',encoding='utf-8')
mayor = -1
sucursal_mayor = ''
mayor_edad = -1
sucursal_mayor_edad = ''
nombre_mayor_edad = ''
total = 0
edad_antofa = 0
trabajadores_antofa = 0
edad_calama = 0
trabajadores_calama = 0
edad_ls = 0
trabajadores_ls = 0
edad_25_30 = 0
trabajador_33 = ''
sucursal_33 = ''
ponderacion = 9999
sucursal_p = ''

linea = arch.readline().strip() 

while linea != '':
    partes = linea.split(',')
    total += int(partes[1])
    if int(partes[1]) > mayor:
        sucursal_mayor = partes[0]
        mayor = int(partes[1])
    if partes[0] == 'Antofagasta':
        trabajadores_antofa += int(partes[1])
        for i in range(0,int(partes[1])):
            linea = arch.readline().strip() 
            partes = linea.split(',')
            if int(partes[1]) > mayor_edad:
                mayor_edad = int(partes[1])
                nombre_mayor_edad = partes[0]
                sucursal_mayor_edad = 'Antofagasta'
            if int(partes[1]) >= 25 and int(partes[1]) <= 30: 
                edad_25_30 += 1
            if int(partes[1]) == 33: 
                trabajador_33 = partes[0]
                sucursal_33 = "Antofagasta"    
            edad_antofa += int(partes[1])
            promedio_antofa = float(round((edad_antofa / trabajadores_antofa),2))
            ponderacion_antofa = float(round(((trabajadores_antofa * 10) + (promedio_antofa / 2)),2))
        if ponderacion_antofa < ponderacion:
            ponderacion = ponderacion_antofa
            sucursal_p = 'Antofagasta'
        
    elif partes[0] == 'Calama':
        trabajadores_calama += int(partes[1])
        for i in range(0,int(partes[1])):
            linea = arch.readline().strip() 
            partes = linea.split(',')
            if int(partes[1]) > mayor_edad:
                mayor_edad = int(partes[1])
                nombre_mayor_edad = partes[0]
                sucursal_mayor_edad = 'Calama'
            if int(partes[1]) >= 25 and int(partes[1]) <= 30:
                edad_25_30 += 1
            if int(partes[1]) == 33:
                trabajador_33 = partes[0]
                sucursal_33 = "Calama"   
            edad_calama += int(partes[1])
            promedio_calama = float(round((edad_calama / trabajadores_calama),2))
            ponderacion_calama = float(round(((trabajadores_calama * 10) + (promedio_calama / 2)),2))
        if ponderacion_calama < ponderacion:
            ponderacion = ponderacion_calama
            sucursal_p = 'Calama'
        
    elif partes[0] == 'La Serena':
        trabajadores_ls += int(partes[1])
        for i in range(0,int(partes[1])):
            linea = arch.readline().strip() 
            partes = linea.split(',')
            if int(partes[1]) > mayor_edad:
                mayor_edad = int(partes[1])
                nombre_mayor_edad = partes[0]
                sucursal_mayor_edad = 'La Serena'
            if int(partes[1]) >= 25 and int(partes[1]) <= 30:
                edad_25_30 += 1
            if int(partes[1]) == 33:
                trabajador_33 = partes[0]
                sucursal_33 = "La Serena"   
            edad_ls += int(partes[1])
            promedio_ls = float(round((edad_ls / trabajadores_ls),2))
            ponderacion_ls = float(round(((trabajadores_ls * 10) + (promedio_ls / 2)),2))
        if ponderacion_ls < ponderacion:
            ponderacion = ponderacion_ls
            sucursal_p = 'La Serena'
    porcentaje_25_30 = float(round(((edad_25_30 / total) * 100),2))
    linea = arch.readline().strip()
    
print(f'La sucursal con mas trabajadores es {sucursal_mayor} con {mayor} trabajadores')

print(f'El promedio de edad en Antofagasta es de {promedio_antofa} años')
print(f'El promedio de edad en Calama es de {promedio_calama} años')
print(f'El promedio de edad en La Serena es de {promedio_ls} años')

print(f'El mayor de los empleados es {nombre_mayor_edad} con {mayor_edad} años y trabaja en {sucursal_mayor_edad}')

print(f'El porcentaje de trabajadores que tienen entre 25 y 30 años es de {porcentaje_25_30}%')

print(f'El empleado que tiene 33 años es {trabajador_33} y trabaja en la sucursal de {sucursal_33}')

print(f'La sucursal con menor ponderacion es {sucursal_p} con una ponderacion de {ponderacion}')