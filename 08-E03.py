#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:31:32 2024

@author: martindroguett
"""
def triangulo(figura):
    base = float(input('Ingrese base: '))
    altura = float(input('Ingrese altura: '))
    area = (base * altura) / 2
    return area

def rectangulo(figura):
    largo = float(input('Ingrese largo: '))
    ancho = float(input('Ingrese ancho: '))
    area = (largo * ancho)
    return area

def circulo(figura):
    radio = float(input('Ingrese radio: '))
    area = 3.14 * radio * radio
    return area

num = int(input('Ingrese cantidad de figuras a calcular: '))
mayor = -1
nombre_mayor = ''
nombre = ''

for i in range (num):
    figura = str(input('Ingrese figura: ')).strip().upper()
    
    if figura == 'TRIANGULO':
        area = triangulo(figura)
        nombre = 'Triángulo'
        
    elif figura == 'RECTANGULO':
        area = rectangulo(figura)
        nombre = 'Rectángulo'
        
    elif figura == 'CIRCULO':
        area = circulo(figura)
        nombre = 'Círculo'
        
    if area > mayor:
        mayor = area
        nombre_mayor = nombre

print(f'La figura mayor fue un {nombre_mayor} con un área de {mayor}')