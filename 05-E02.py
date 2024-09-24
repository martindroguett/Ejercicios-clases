#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:59:25 2024

@author: martindroguett
"""
arch = open('Vuelos.txt','r',encoding = 'utf-8')
vuelos = 0
stgo_d = 0
pasajeros_stgo_antofa = 0
vuelos_stgo_antofa = 0
promedio = 0
mayor = -1
destino_mayor = ''
menor = 9999
origen_menor = ''
vuelos_p = 0
porcentaje = 0

linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    vuelos += 1
    if partes[1] == 'Santiago':
        stgo_d += 1
    if partes[0] == 'Santiago' or partes[0] == 'Antofagasta':
        vuelos_stgo_antofa += 1
        pasajeros_stgo_antofa += int(partes[2])
    if int(partes[2]) > mayor:
        mayor = int(partes[2])
        destino_mayor = partes[1]
    if int(partes[2]) < menor:
        menor = int(partes[2])
        origen_menor = partes[0]
    if int(partes[2]) < 100:
        vuelos_p += 1
    linea = arch.readline().strip()

promedio = float(round((pasajeros_stgo_antofa / vuelos_stgo_antofa),2))
porcentaje = float(round(((vuelos_p / vuelos) * 100),2))

print(f'La cantidad de vuelos realizados es de {vuelos}')
print(f'La cantidad de vuelos con destino a Santiago es de {stgo_d}')
print(F'El promedio de pasajeros en viajes con origen de Santiago o Antofagasta es {promedio}')
print(f'La ciudad de destino con más pasajeros es {destino_mayor} con {mayor} pasajeros')
print(f'La ciudad de origen con menos pasajeros es {origen_menor} con {menor} pasajeros')
print(f'El porcentaje de vuelos con menos de 100 personas es de {porcentaje}%')
