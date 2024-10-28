#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:48:28 2024

@author: martindroguett
"""

def ingresar_numero():
    num = int(input('Ingrese número: '))
    return num

def procesar(n):
    if n % 7 == 0:
        return True
    else:
        return False
    
def escribir_resultado(r):
    if r == True:
        print('El número ingresado es divisible por 7.')
    else:
        print('El número ingresado no es divisible por 7.')
        
def main():
    n = ingresar_numero()
    r = procesar(n)
    escribir_resultado(r)
    
main()