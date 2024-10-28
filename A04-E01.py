#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:53:01 2024

@author: martindroguett
"""

arch = open('juegos.txt','r',encoding='utf-8')

gow = 0
gow_j = 0
fc = 0
fc_j = 0
cod = 0
cod_j = 0

mas = 0
mas_juego = ''

rapido = 999999
rapido_juego = ''
rapido_j = ''

linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    
    if partes[1] == 'god of war':
        gow += int(partes[2])
        gow_j += 1
        
    elif partes[1] == 'call of duty':
        cod += int(partes[2])
        cod_j += 1
    
    elif partes[1] == 'far cry':
        fc += int(partes[2])
        fc_j += 1
        
    if gow > mas:
        mas = gow
        mas_juego = 'God of War'
        
    elif cod > mas:
        mas = cod
        mas_juego = 'Call of Duty'
        
    elif fc > mas:
        mas = fc
        mas_juego = 'Far Cry'
        
    if int(partes[2]) < rapido:
        rapido = int(partes[2])
        rapido_juego = partes[1]
        rapido_j = partes[0]
        
    linea = arch.readline().strip()

gow_p = round((gow/gow_j),2)
cod_p = round((cod/cod_j),2)
fc_p = round((fc/fc_j),2)
    
print(f'El promedio de horas jugadas a God of War fueron de {gow_p}')
print(f'El promedio de horas jugadas a Call of Duty fueron de {cod_p}')
print(f'El promedio de horas jugadas a Far Cry fueron de {fc_p}')
print(f'El juego más jugado es {mas_juego} con {mas} horas')
print(f'El jugador que más rápido terminó un juego fue {rapido_j} que terminó {rapido_juego} en {rapido} horas')