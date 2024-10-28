#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:35:33 2024

@author: martindroguett
"""
suma = 0
mayor = -1
producto_mayor = ''

def total(articulo,cantidad):
    arch_p = open('precios.txt','r',encoding='utf-8')
    linea_p = arch_p.readline().strip()
    while linea_p != '':    
        partes_p = linea_p.split(', ')
        cosa_p = str(partes_p[0])
        precio_p = int(partes_p[1])
        if cosa_p == cosa_a:
            precio = precio_p * cantidad_a
            return precio
        linea_p = arch_p.readline().strip()


articulos = open('artículos.txt','r',encoding='utf-8')
linea_a = articulos.readline().strip()
while linea_a != '':    
    partes_a = linea_a.split(', ')
    cosa_a = str(partes_a[0])
    cantidad_a = int(partes_a[1])
    precio = total(cosa_a,cantidad_a)
    
    suma += precio
    
    if precio > mayor:
        mayor = precio
        producto_mayor = cosa_a
    
    linea_a = articulos.readline().strip()

print(f'El total que se ganará en el remate es de ${suma}')
print(f'El producto qué más ganancia entregará es {producto_mayor} con ${mayor}')
