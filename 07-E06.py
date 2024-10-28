#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:34:34 2024

@author: martindroguett
"""

def calcular_tiempo(d,v):
    tiempo = float(d / v)
    return tiempo

def dividir_distancia(distancia):
    distancia = float(distancia / 2)
    return distancia

def aumentar_velocidad(v):
    v = float(v * 1.5)
    return v

def iterar(d,v):
    tiempo_total = 0
    tiempo_round = 1
    d_round = 10
    while (d > 0.1) and (tiempo_round != 0) and (d_round > 0.39):
        d = dividir_distancia(d)
        tiempo = calcular_tiempo(d,v)
        tiempo_total += tiempo
        tiempo_round = round(tiempo,2)
        d_round = round(d,2)
        v_round = round(v,2)
        print(f'En recorrer {d_round} me demoro {tiempo_round} con velocidad {v_round}')
        v = aumentar_velocidad(v)
    return tiempo_total

def main(d,v):
    print(f'Vamos a comenzar con d= {d} y v= {v}')
    tiempo = round(iterar(d,v),2)
    print(f'Tiempo total {tiempo}')

arch = open('datos.txt','r',encoding='utf-8')
linea = arch.readline().strip()
d = int(linea)
linea = arch.readline().strip()
v = int(linea)

main(d,v)
