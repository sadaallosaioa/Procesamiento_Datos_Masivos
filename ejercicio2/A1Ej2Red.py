#!/usr/bin/python3

import sys 


''' 
Reducer del Ejercicio 2
Creado por Saioa Sada Allo
''' 

subproblema = None
citantes=[]

for claveValor in sys.stdin: 
	citada, citante = claveValor.split("\t", 1)
	citada = int(citada)
	citante = int(citante)
	
	
	#El primer subproblema la primera patente citada   
	if subproblema == None: 
		subproblema = citada 
		citantes.append(citante)

	elif subproblema == citada: 
		citantes.append(citante)
	#si ya acabamos con el subproblema
	else:
		citantes.sort()
		print("%s\t%s" % (subproblema, ','.join([str(el) for el in citantes])))
		#Pasamos al siguiente subproblema
		subproblema = citada 
		citantes=[citante]
		
#el anterior bucle no emite el ultimo subproblema
citantes=citantes.sort()
print("%s\t%s" % (citada, citantes)) 
