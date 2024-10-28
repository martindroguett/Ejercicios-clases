#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:00:13 2024

@author: martindroguett
"""

arch = open('archivo.txt','r')

linea = arch.readline().strip()
cantidad = int(linea)

for i in range (cantidad):
    linea = arch.readline().strip()
    numero = int(linea)
    print('Hemos leído el número',numero)
    
arch.close()