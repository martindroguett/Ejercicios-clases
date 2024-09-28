# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:47:29 2024

@author: catal
"""
arch = open("vuelos.txt", 'r' , encoding = 'utf-8')
total = 0
sant = 0
vuelo_as = 0
pasaj_as = 0
mayor = -1
mayor_p = ''
menor_p = ''
menor = 99999
porc = 0
vuelos_p = 0

linea = arch.readline().strip()
while linea != '':
    partes = linea.split(',')
    origen = partes [0]
    destino = partes [1]
    pasajeros = int(partes[2])
    total += 1
    if destino == "Santiago":
        sant += 1
    if origen == "Antofagasta" or origen == "Santiago":
        vuelo_as +=1
        pasaj_as += pasajeros
        promedio = float(round((pasaj_as/vuelo_as),2))
    if pasajeros > mayor:
        mayor = pasajeros
        mayor_p = destino
    if pasajeros < menor:
        menor = pasajeros
        menor_p = origen
    if pasajeros < 100:
        vuelos_p += 1
        porc = float(round(((vuelos_p/total)*100),2))
    linea = arch.readline().strip()
print(f'el total de vuelos realizados fue {total}')
print(f'los vuelos a santiago fueron {sant}')
print(f'el promedio de pasajeros desde Antofagasta o Santiago fue de {promedio}')
print(f'la ciudad de destino con más pasajeros fue {mayor_p}')
print(f'la ciudad de origen con menos pasajeros fue {menor_p}')
print(f'el porcentaje de vuelos con menos de 100 personas fue de {porc}')


        
        
    
