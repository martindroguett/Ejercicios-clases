#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:39:28 2024

@author: martindroguett
"""

arch = open('resultados_tarreo.txt','r',encoding='utf-8')
linea = arch.readline().strip()
arch2 = open('concursantes.txt','r',encoding='utf-8')

joven = 9999
joven_n = ''

mas = 0
mas_n = ''
mas_juego = ''

while linea != '':
    partes_juego = linea.split(',')
    jugadores = int(partes_juego[1])
    
    juego = partes_juego[0]
    ganador_tiempo = 99999999
    ganador = ''
    ganador_apuesta = 0
    
    for i in range(0,jugadores):
    
        linea = arch.readline().strip()
        linea2 = arch2.readline().strip()
        partes_jugador = linea.split(', ')
        partes_concursante = linea2.split('./')
        
        nombre = partes_jugador[0]
        tiempo = int(partes_jugador[1])
        apuestas = int(partes_jugador[3])
        total_apuestas = 0
        
        for j in range(0,apuestas):
            total_apuestas += int(partes_jugador[4+j])
            
        if partes_jugador[2] == 'Legal':
            
            if tiempo < ganador_tiempo:
                ganador_tiempo = tiempo
                ganador = nombre
                ganador_apuesta = total_apuestas
                
            if int(partes_concursante[1]) < joven and (ganador == nombre):
                joven = int(partes_concursante[1])
                joven_n = nombre
                
        if int(partes_concursante[2]) > mas:
            mas = int(partes_concursante[2])
            mas_n = nombre
            mas_juego = juego
                    
    print(f'{juego}: ')
    print(f'Ganador: {ganador} con un tiempo de {ganador_tiempo}')
    print(f'Apuesta total a {ganador}: {ganador_apuesta}')
    print('======================================================')
         
    linea = arch.readline().strip()
    
print(f'En toda la competencia, el ganador más joven es {joven_n} con {joven} años')
print(f'En toda la competencia, el jugador que más hora le dedicó a un juego fue {mas_n} con {mas} horas en {mas_juego}')