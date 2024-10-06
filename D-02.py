# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:05:27 2024

@author: catal
"""
arch = open('fondas.txt', 'r', encoding='utf-8')
linea = arch.readline().strip()

precio_total = 0
cant_productos = 0
ventas_totales = 0
costo_total = 0
ganancia = 0
nombre = linea
cost_anticuchos = pre_anticuchos = 0
cost_churrascas = pre_churrascas = 0
cost_empanadas = pre_empanadas = 0
cost_mote = pre_mote = 0
cost_bebida = pre_bebida = 0
cost_chicha = pre_chicha = 0
cost_terremoto = pre_terremoto = 0
cost_cerveza = pre_cerveza = 0

linea = arch.readline().strip()
while linea != "Ventas":
    cant_productos += 1
    partes = linea.split('/')
    nombre_producto = partes[0].strip()
    coste_preparacion = int(partes[1])
    precio_venta = int(partes[2])

    if nombre_producto == "Anticuchos":
        cost_anticuchos = coste_preparacion
        pre_anticuchos = precio_venta
    elif nombre_producto == "Churrascas":
        cost_churrascas = coste_preparacion
        pre_churrascas = precio_venta
    elif nombre_producto == "Empanadas":
        cost_empanadas = coste_preparacion
        pre_empanadas = precio_venta
    elif nombre_producto == "Mote con Huesillo":
        cost_mote = coste_preparacion
        pre_mote = precio_venta
    elif nombre_producto == "Bebida":
        cost_bebida = coste_preparacion
        pre_bebida = precio_venta
    elif nombre_producto == "Chicha":
        cost_chicha = coste_preparacion
        pre_chicha = precio_venta
    elif nombre_producto == "Terremoto":
        cost_terremoto = coste_preparacion
        pre_terremoto = precio_venta
    elif nombre_producto == "Cerveza":
        cost_cerveza = coste_preparacion
        pre_cerveza = precio_venta
    
    linea = arch.readline().strip()

linea = arch.readline().strip()
while linea != "":
    partes = linea.split(':')
    producto = partes[0].strip()
    cantidad_vendida = int(partes[1].strip())
    if producto == "Anticuchos":
       costo_total += (cost_anticuchos * cantidad_vendida)
       ventas_totales += (pre_anticuchos * cantidad_vendida)
    elif producto == "Churrascas":
        costo_total += (cost_churrascas * cantidad_vendida)
        ventas_totales += (pre_churrascas * cantidad_vendida)
    elif producto == "Empanadas":
        costo_total += (cost_empanadas * cantidad_vendida)
        ventas_totales += (pre_empanadas * cantidad_vendida)
    elif producto == "Mote con Huesillo":
        costo_total += (cost_mote * cantidad_vendida)
        ventas_totales += (pre_mote * cantidad_vendida)
    elif producto == "Bebida":
        costo_total += (cost_bebida * cantidad_vendida)
        ventas_totales += (pre_bebida * cantidad_vendida)
    elif producto == "Chicha":
        costo_total += (cost_chicha * cantidad_vendida)
        ventas_totales += (pre_chicha * cantidad_vendida)
    elif producto == "Terremoto":
        costo_total += (cost_terremoto * cantidad_vendida)
        ventas_totales += (pre_terremoto * cantidad_vendida)
    elif producto == "Cerveza":
        costo_total += (cost_cerveza * cantidad_vendida)
        ventas_totales += (pre_cerveza * cantidad_vendida)
    
    linea = arch.readline().strip()

ingreso_ventas = ventas_totales
ganancia = ventas_totales - costo_total


print(nombre)
print(f'Cantidad de productos: {cant_productos}')
print(f'Total costo de preparación: ${costo_total}')
print(f'Total ingreso por ventas: ${ingreso_ventas}')
print(f'Total ganancias: ${ganancia}')

