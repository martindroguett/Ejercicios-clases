#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:59:22 2024

@author: martindroguett
"""

def analisis(archivo,juego):
    arch = open(f'{archivo}','r',encoding='utf-8')
    linea = arch.readline().strip()
    coincide = 0
    mas = 0
    mas_j = ''
    while linea != '':
        partes = linea.split(', ')
        
        if juego.lower() == partes[1].lower():
            coincide += 1
            if int(partes[2]) > mas:
                mas = int(partes[2])
                mas_j = partes[0]
        linea = arch.readline().strip()
    
    if coincide != 0:
        print(f'En el archivo {archivo} el jugador con más horas en {juego} es {mas_j} con {mas} horas.')
    else:
        print(f'No se encontraron jugadores para el juego {juego} en el archivo {archivo}.')
        
archivo = input('Ingrese archivo: ')
juego = input('Ingrese juego: ')

analisis(archivo,juego)