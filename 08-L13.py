#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:06:18 2024

@author: martindroguett
"""

def suma(archivo):
    arch = open(f'{archivo}','r',encoding='utf-8')
    linea = arch.readline().strip()
    suma = 0
    
    while linea != '':
        suma += int(linea)
        linea = arch.readline().strip()
    return suma
        
def lineas(archivo):
    arch = open(f'{archivo}','r',encoding='utf-8')
    lineas = 0
    linea = arch.readline().strip()
    while linea != '':
        lineas += 1
        linea = arch.readline().strip()
    return lineas
        
def promedio():
    arch = str(input('Ingrese archivo: '))
    s = suma(arch)
    c = lineas(arch)
    promedio = round((s/c),2)
    print(f'El promedio es {promedio}')
    
promedio()