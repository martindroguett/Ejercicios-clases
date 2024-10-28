#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:42:24 2024

@author: martindroguett
"""

arch = open ('nacimientos.txt', 'r')

linea = arch.readline().strip()
lineas = 0

while linea != "":
    lineas += 1
    partes = linea.split (',')
    nombre = partes [0]
    ciudad = partes [1]
    a = partes [2]
    
    print('Nombre',nombre)
    print('Ciudad',ciudad)
    print('Año',a)
    print(f'Informacion obtenida de la línea: {lineas}')

    linea = arch.readline().strip ()

print('En el código hay un total de {lineas} líneas.')

arch.close()