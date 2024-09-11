#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:49:15 2024

@author: martindroguett
"""
x = str(input('Ingrese nombres (Para finalizar escriba "FIN"): ')).strip().upper()
berta = 0
juan = 0
jorge = 0
while x != "FIN":
    if x == "JORGE":
        jorge += 1
    elif x == "JUAN":
        juan += 1
    elif x == "BERTA":
        berta += 1
    x = str(input('Ingrese nombres (Para finalizar escriba "FIN"): ')).strip().upper()
print(f"Se ingresaron {berta} estudiante/s con el nombre Berta, {juan} con el nombre Juan y {jorge} con el nombre Jorge.")