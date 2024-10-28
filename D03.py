#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:42:12 2024

@author: martindroguett
"""
arch = open('data-candy.txt','r',encoding='utf-8')
secuencia = arch.readline().strip()
partes_sec = secuencia.split(',')

def analisis(secuencia):
    linea = arch.readline().strip()
    linea = arch.readline().strip() #Dos veces para llegar a la linea de los dulces
    
    sugar = 9999999
    sugar_name = ''
    price = 9999999
    price_name = ''
    win = -1
    win_name = ''
    
    while linea != '':
        partes_dul = linea.split(';')
        unos = 0 #Cantidad de 1 en secuencia
        coincide = 0 #Cantidad de Trues
        
        
        for i in range(0,9): #Lee la secuencia de una misma linea
            if partes_sec[i] == '1':
                unos += 1
                
            if str(partes_dul[1+i]) == str(partes_sec[i]) == '1':
                coincide += 1
                       
        if unos == coincide:
            if float(partes_dul[10]) < sugar:
                sugar = float(partes_dul[10])
                sugar_name = partes_dul[0]
            if float(partes_dul[11]) < price:
                price = float(partes_dul[11])
                price_name = partes_dul[0]
            if float(partes_dul[12]) > win:
                win = float(partes_dul[12])
                win_name = partes_dul[0]
                
        linea = arch.readline().strip()
        
    sugar_p = round((sugar * 100))
    price_p = round((price * 100))
    win_p = round((win * 100))
        
    print(f'Menor sugarpercent: {sugar_name} con {sugar_p}%')
    print(f'Menor pricepercent: {price_name} con {price_p}%')
    print(f'Mayor winpercent: {win_name} con {win_p}%')
    
analisis(secuencia)