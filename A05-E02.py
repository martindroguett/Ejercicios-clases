#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:29:37 2024

@author: martindroguett
"""

def palindromo(palabra):
    letras = 0
    palindromo = True
    palabra.split()
    
    for i in palabra:
        letras += 1
        
    if (letras % 2) == 0:
        for j in range(letras):
            if palabra[j] != palabra[letras-j-1]:
                palindromo = False
                
    elif (letras % 2) != 0:
        letrass = letras // 2
        for k in range(letrass):
            if palabra[k] != palabra[letras-k-1]:
                palindromo = False
    
    return palindromo

palabra = input('Ingrese palabra: ')

palindromoo = palindromo(palabra)

if palindromoo == True:
    print('Es palindromo!')
else: print('No es palindromo')

arch1 = open('palabras.txt','r',encoding='utf-8')
linea = arch1.readline().strip()
palindromos = 0

while linea != '':
    palindromoo = palindromo(linea)
    if palindromoo == True:
        palindromos += 1

    linea = arch1.readline().strip()
print(f'El número de palabras palíndromas en el archivo palabras.txt es {palindromos}')

arch2 = open('palabras_2.txt','r',encoding='utf-8')
linea = arch2.readline().strip()
palindromos = 0

while linea != '':
    palindromoo = palindromo(linea)
    if palindromoo == True:
        palindromos += 1
        
    linea = arch2.readline().strip()
    
print(f'El número de palabras palíndromas en el archivo palabras_2.txt es {palindromos}')

