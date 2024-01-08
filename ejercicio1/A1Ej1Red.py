#!/usr/bin/python3

import sys 


''' 
Reducer del Ejercicio 1 
Creado por Saioa Sada Allo
''' 

subproblema = None
sumagastos = 0 
sumavisitas = 0

for claveValor in sys.stdin: 
	ct, gasto, visitas = claveValor.split("\t", 2)
	gasto = float(gasto)
	visitas = float(visitas)
	
	
	#El primer subproblema es el primer comprador_tienda   
	if subproblema == None: 
		subproblema = ct 
		sumagastos = 0 
		sumavisitas = 0
	
	#si el comprador_tienda es el del subpoblema actual, acumulamos la suma gastada 
	# y la suma de visitas
	if subproblema == ct: 
		sumagastos=sumagastos+gasto
		sumavisitas = sumavisitas+visitas
	#si ya acabamos con el subproblema, calculamos el promedio:
	else:
		media=sumagastos/sumavisitas
		print("%s;%s" % (subproblema, media))
		#Pasamos al siguiente subproblema
		subproblema = ct
		sumagastos = gasto
		sumavisitas = visitas


#el anterior bucle no emite el ultimo subproblema
media=sumagastos/sumavisitas
print("%s;%s" % (subproblema, media)) 
