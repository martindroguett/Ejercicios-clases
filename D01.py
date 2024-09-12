# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:41:44 2024

@author: catalina
"""
num = int(input("Ingrese Número: ")) 
c = 0 # cant de primos
s = 0 # suma de primos
while num <= 1:
    num = int(input("Debe ser mayor a 1, Reingrese Número: "))
print("Detalle Primos:")
for i in range(0, (num + 1)):
     cont = 0
     for n in range(1, i):
         if i % n == 0:
             cont += 1
     if cont < 2 and i>1:
         print(i)
         c += 1
         s += i
print(f"Contador primos: {c}")
print(f"Suma primos: {s}")
     
           

    
     
      
            

    
    
 
    
    
