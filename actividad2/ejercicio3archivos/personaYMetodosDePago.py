#!/usr/bin/python3 
import sys
from pyspark.sql import SparkSession

''' 
Creado por Saioa Sada Allo
''' 

#funcion que utilizo en el map: 
#separar al cliente y el gasto 
#(cero si es con tarjeta o si no es superior a 1500)
#(Uno si es sin tarjeta y mayor a 1500)
def funcion1a(linea):
  valores= linea.split(";")
  valores[2]=float(valores[2])
  if valores[1]!='Tarjeta de crédito' and valores[2]>1500:
    return([valores[0], 1])
  else:
    return([valores[0], 0])

def funcion1b(linea):
  valores= linea.split(";")
  valores[2]=float(valores[2])
  if valores[1]!='Tarjeta de crédito' and valores[2]<=1500:
    return([valores[0], 1])
  else:
    return([valores[0], 0])

#inicializacion
spark = SparkSession.builder.appName('comprasSinTDCMayorDe1500').getOrCreate()

entrada = sys.argv[1] 
salida1 = sys.argv[2]
salida2 = sys.argv[3]

# cargamos los datos de entrada 
datosEntrada = spark.sparkContext.textFile(entrada) 

# Aunque no creo que influya en el rendimiento, primero llegaré a la 
# solución del primer problema y luego lo mismo con el segundo

# Transformaciones del RDD inicial:
datosSalida1 = datosEntrada.map(funcion1a).reduceByKey(lambda x, y: x + y)
# Guardado de la solución:
datosSalida1.saveAsTextFile(salida1)

# Lo mismo para el segundo problema:
datosSalida2 = datosEntrada.map(funcion1b).reduceByKey(lambda x, y: x + y)

datosSalida2.saveAsTextFile(salida2)

# detenemos el Spark session
spark.stop()