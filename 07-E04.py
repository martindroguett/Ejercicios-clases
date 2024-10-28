#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:17:11 2024

@author: martindroguett
"""

def anillos(numero):
    anillos = 0
    for i in numero:
        if (i == '9') or (i == '6') or (i == '0'):
            anillos += 1
        elif i == '8':
            anillos += 2
    return anillos

mas = 'si'
while mas != 'no':
    
    num = str(input('Ingrese el número a evaluar: ')).strip()
    
    print('Los anillos presentes en el número son:',anillos(num))
    
    mas = str(input('¿Desea evaluar otro número?: ')).strip().lower()
