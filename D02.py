#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:58:00 2024

@author: martindroguett
"""

arch = open('fondas.txt','r',encoding='utf-8')

nombre = ''
productos = 0
costo = 0
venta = 0
ganancia = 0

Anticuchos = (0,0)
Churrascas = (0,0)
Empanadas = (0,0)
Mote = (0,0)
Bebida = (0,0)
Chicha = (0,0)
Terremoto = (0,0)
Cerveza = (0,0)

linea = arch.readline().strip()
nombre = linea

linea = arch.readline().strip()
while linea != 'Ventas':
    partes = linea.split('/')
    if partes[0] == 'Anticuchos':
        Anticuchos = (partes[1],partes[2]) 
    elif partes[0] == 'Churrascas':
        Churrascas = (partes[1],partes[2])
    elif partes[0] == 'Empanadas':
        Empanadas = (partes[1],partes[2])
    elif partes[0] == 'Mote con Huesillo':
        Mote = (partes[1],partes[2])
    elif partes[0] == 'Bebida':
        Bebida= (partes[1],partes[2])
    elif partes[0] == 'Chicha':
        Chicha = (partes[1],partes[2])
    elif partes[0] == 'Terremoto':
        Terremoto = (partes[1],partes[2])
    elif partes[0] == 'Cerveza':
        Cerveza = (partes[1],partes[2])
    productos += 1
    linea = arch.readline().strip()

linea = arch.readline().strip()

while linea != '':
    partes = linea.split(':')
    if partes[0] == 'Anticuchos':
        costo += int(Anticuchos[0]) * int(partes[1])
        venta += int(Anticuchos[1]) * int(partes[1])
    elif partes[0] == 'Churrascas':
        costo += int(Churrascas[0]) * int(partes[1])
        venta += int(Churrascas[1]) * int(partes[1])
    elif partes[0] == 'Empanadas':
        costo += int(Empanadas[0]) * int(partes[1])
        venta += int(Empanadas[1]) * int(partes[1])
    elif partes[0] == 'Mote con Huesillo':
        costo += int(Mote[0]) * int(partes[1])
        venta += int(Mote[1]) * int(partes[1])
    elif partes[0] == 'Bebida':
        costo += int(Bebida[0]) * int(partes[1])
        venta += int(Bebida[1]) * int(partes[1])
    elif partes[0] == 'Chicha':
        costo += int(Chicha[0]) * int(partes[1])
        venta += int(Chicha[1]) * int(partes[1])
    elif partes[0] == 'Terremoto':
        costo += int(Terremoto[0]) * int(partes[1])
        venta += int(Terremoto[1]) * int(partes[1])
    elif partes[0] == 'Cerveza':
        costo += int(Cerveza[0]) * int(partes[1])
        venta += int(Cerveza[1]) * int(partes[1])
    linea = arch.readline().strip()

ganancia = int(venta - costo)

print(nombre)
print(f"Cantidad de productos: {productos}")
print(f'Total costo de preparación: ${costo}')
print(f'Total ingreso por ventas: ${venta}')
print(f'Total ganancias: ${ganancia}')