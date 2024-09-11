#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:27:50 2024

@author: martindroguett
"""
print("Buddy se encuentra en la casilla (0,0)")
print("Considere que U = 1 metro hacia arriba / D = 1 metro hacia abajo / R = 1 metro hacia la derecha / L = 1 metro hacia la izquierda y que Buddy solo puede caminar en su mundo de 6x6 metros y siempre empieza en la esquina superior izquierda")
secuencia = str(input("Ingrese una secuencia de movimiento: ")).upper()
horizontal = 0
vertical = 0
error = False

for x in secuencia:
    if x != "U" and x != "D" and x != "R" and x != "L":
        error = True
    if x == "U":
        vertical += 1
        if vertical > 0:
            break
    elif x == "D":
        vertical -= 1
        if vertical < 5:
            break
    elif x == "R" :
        horizontal += 1
        if horizontal > 5:
            break
    elif x == "L":
        horizontal -= 1
        if horizontal < 0:
            break

horizontal_ia = "R" * horizontal
vertical_ia = "D" * (-vertical)

if not (horizontal > -1 and horizontal < 6 and vertical < 1 and vertical > -6) and error == False:
    print("Buddy se cayó del mundo y murió")
elif error == True:
    print("Buddy no entendió y se fue")
elif secuencia == "":
    print("Se acabó, gracias por participar!")
else: 
    print(f"Buddy está en la posición ({horizontal},{vertical})")
    if horizontal == 0 and vertical == 0:
        print("Buddy volvió a su posición inicial")
    else: print(f"El camino más corto es: {horizontal_ia}{vertical_ia}")