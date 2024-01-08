#!/usr/bin/python3

import sys 

 

''' 

Mapper de la actividad 1, ejercicio2: Tras ignorar las cabeceras 
se invierte el orden de cada dupla y se separan con /t
Creado por Saioa Sada Allo

'''
i=0 
for linea in sys.stdin:
  linea = linea.strip()
  if i!=0:
    citante , citada = linea.split(",", 1)
    print("%s\t%s" % (citada, citante))
  i=1
