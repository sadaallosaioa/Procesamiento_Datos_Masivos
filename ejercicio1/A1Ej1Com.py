#!/usr/bin/python3

import sys 


''' 
Combiner del Ejercicio 1 
Creado por Saioa Sada Allo
''' 


subproblema = None 
sumagastada = 0
visitas = 0


for claveValor in sys.stdin: 
	ct, cant = claveValor.split("\t", 1) 
	
	#convertimos la cantidad gastada a float 
	cant = float(cant) 
	
	#El primer subproblema es el primer comprador_tienda   
	if subproblema == None: 
		subproblema = ct 
		sumagastada = 0 
		visitas = 0
	
	#si el comprador_tienda es el del subpoblema actual, acumulamos la cantidad gastada 
	# y aumentamos el contador de visitas
	if subproblema == ct: 
		sumagastada=sumagastada+cant
		visitas = visitas+1 
	else: #si ya acabamos con el subproblema, emitimos            
		print("%s\t%s\t%s" % (subproblema, sumagastada, visitas)) 

		#Pasamos al siguiente subproblema  
		subproblema = ct 
		sumagastada = cant
		visitas = 1 
#el anterior bucle no emite el ultimo subproblema
print("%s\t%s\t%s" % (subproblema, sumagastada, visitas)) 
