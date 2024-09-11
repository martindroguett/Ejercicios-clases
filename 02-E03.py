#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:12:49 2024

@author: martindroguett
"""
figura = str(input("Escoje una figura geométrica (Triángulo, Círculo o Cubo):"))
if str(figura) == "Triángulo":
    lado_1_tr = float(input("¿Cuánto mide el lado 1 o su base?:"))
    lado_2_tr = float(input("¿Cuánto mide el lado 2?:"))
    lado_3_tr = float(input("¿Cuánto mide el lado 3?:"))
    if lado_1_tr == lado_2_tr and lado_2_tr == lado_3_tr:
        area_tr_eq = (((3 ** (1 / 2)) * (lado_1_tr ** 2) / 4))
        print("El área del triángulo es:", area_tr_eq, "u²")
    elif lado_1_tr != lado_2_tr and lado_2_tr == lado_3_tr:
        mitad_base = lado_1_tr / 2
        altura_tr = (((lado_2_tr ** 2) - (mitad_base ** 2)) ** (1 / 2))
        area_tr = ((lado_1_tr * altura_tr) / 2)
        print("El área del triángulo es:", area_tr, "u²")      
    else: 
        altura_tr = float(input("¿Cuál es su altura?:"))
        area_tr = ((lado_1_tr * altura_tr) / 2)
        print("El área del triángulo es:", area_tr, "u²")
        
if str(figura) == "Círculo":
    radio = float(input("¿Cuál es el radio?:")) 
    area_ci = (2 * radio)
    print(f"El área del círculo es: {area_ci}π", "u²") 
    
if str(figura) == "Cubo":
    lado_cu = float(input("¿Cuánto mide su lado?:"))
    area_cara = lado_cu * lado_cu
    area_cu = 6 * area_cara
    print (f"El área del cubo es: {area_cu} u²")

else:
    print("No sé sobre esa figura :( ¡Prueba con una de estas: Triángulo, Círculo o Cubo!")
    