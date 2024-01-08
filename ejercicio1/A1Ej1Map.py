#!/usr/bin/python3

import sys 

 

''' 

Mapper de la actividad 1: mira las ternas de (comprador, tienda, gasto)
y extrae duplas (comprador_tienda,gasto)
Creado por Saioa Sada Allo

''' 

#Por cada medida de temp emitimos los pares <anyo, temp> 
for linea in sys.stdin: 
	linea = linea.strip() 
	comprador , tienda, gasto = linea.split(";", 2) 
	print("%s\t%s" % (comprador+";"+tienda, gasto)) 
