#!/usr/bin/python3 
import sys
from pyspark.sql import SparkSession

''' 
Creado por Saioa Sada Allo
''' 

#funcion que utilizo en el map: 
#separar al cliente y el gasto (cero si no es con tarjeta)
def funcion1(linea):
  valores= linea.split(";")
  if valores[1]!='Tarjeta de crédito':
    return([valores[0], 0])
  else:
    return([valores[0], float(valores[2])])
 

#inicializacion
spark = SparkSession.builder.appName('personaGastosConTarjetaCredito').getOrCreate()

entrada = sys.argv[1] 
salida = sys.argv[2]

# cargamos los datos de entrada 
datosEntrada = spark.sparkContext.textFile(entrada) 

# Recurro a lambda para el reducer:
suma = datosEntrada.map(funcion1).reduceByKey(lambda x, y: x + y) 

# guardamos la salida 
suma.saveAsTextFile(salida)

# detenemos el Spark session
spark.stop()