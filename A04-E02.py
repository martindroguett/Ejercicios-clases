#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:19:40 2024

@author: martindroguett
"""

arch = open('vuelos.txt','r',encoding='utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    
    marca = partes[0]
    menor = 999999
    m_menor = ''
    mas = 0
    m_mas = ''
    total = 0
    distancia = 0
    helice = 0
    reaccion = 0
    
    for i in range (int(partes[1])):
        linea = arch.readline().strip()
        partes = linea.split(',')
        total += 1
        distancia += int(partes[3])
        
        if int(partes[1]) < menor:
            menor = int(partes[1])
            m_menor = partes[0]
            
        if int(partes[2]) > mas:
            mas = int(partes[2])
            m_mas = partes[0]
            
        if partes[4] == 'helice':
            helice += 1
        
        elif partes[4] == 'reaccion':
            reaccion += 1
        
    promedio = round((distancia/total),2)
    p_helice = round((helice/total)*100,2)
    p_reaccion = round((reaccion/total)*100,2)
    
    print(marca)
    print(f'El modelo con menor distancia de despegue es {m_menor} con {menor} metros')
    print(f'El modelo con mayor capacidad de personas es {m_mas} pudiendo llevar a {mas} personas')
    print(f'El promedio de distancia de vuelo es de {promedio} metros')
    print(f'El porcentaje de motores tipo helice es de {p_helice}% y los de reacción es de {p_reaccion}%')
    
    linea = arch.readline().strip()