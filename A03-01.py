# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:32:16 2024

@author: LabCivil6-Pc22
"""
menor = 9999
n_menor = ""
mayor = -1
n_mayor = ""
print("veamos qué mascotas fue más rápida!! :D Para finalizar el programa ingresa (-1)")
tiempo = int(input("Ingresa su tiempo (en segundos): "))
while tiempo != -1:
        n = input("¿Cuál es el nombre de tu mascota? ")
        if tiempo < menor:
            menor = tiempo
            n_menor = n
        if tiempo > mayor:
            mayor = tiempo
            n_mayor = n
        tiempo = int(input("Ingresa su tiempo (en segundos): "))
if (n_menor == n_mayor and menor == mayor):
    print("no se puede calcular el menor :(")
elif (mayor == menor) and (n_menor != n_mayor):
    print(f'tenemos un empate!! con {menor} (s)')
else:
    print(f'La mascota más rápida fue {n_menor} con un tiempo de {menor}, felicidades!!')
    print(f'La mascota más lenta fue {n_mayor} con un tiempo de {mayor}')
     
