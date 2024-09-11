#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:00:14 2024

@author: martindroguett
"""
import time
segundos = int(input("Elige una cantidad de segundos para crear un contador:"))
minutos = segundos // 60
segundo = segundos % 60
print(f"{minutos}:{segundo}")
while segundos != 0:
    time.sleep(1)
    segundos -= 1
    minutos = segundos // 60
    segundo = segundos % 60
    print(f"{minutos}:{segundo}") 
print("El contador terminó!")