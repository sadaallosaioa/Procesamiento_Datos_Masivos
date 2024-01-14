#!/usr/bin/python3 
import sys
from pyspark.sql import SparkSession
''' 
Creado por Saioa Sada Allo
''' 
#inicializacion
spark = SparkSession.builder.appName('CategoriaDeVideosMenosVista').getOrCreate()
sc = spark.sparkContext

entrada = sys.argv[1] 
salida = sys.argv[2]

# Cargamos, en un RDD de archivos, todos los archivos de la carpeta 
# solicitada, excluyendo el log.txt
rdd1_sin_log= spark.sparkContext.wholeTextFiles(entrada).filter(lambda x: 'log.txt' not in x[0])
# Concatenamos los registros de todos los ficheros, creando un solo RDD ya de datos:
rdd2unido = rdd1_sin_log.flatMap(lambda x: x[1].split("\n"))

# Defino una funcion que utilizaré en el próximo map...
# para quedarme con solo las duplas que me interesan:
def funcion1(linea):
  valores= linea.split("\t")
  return([valores[3], int(valores[5])])

# En la siguiente orden:
# 1º Filtro, eliminando los registros incompletos (con menos de 16 campos)
# 2º De cada registro, me quedo con solo las duplas (categoría, nº de vistas)
# 3º Con ReduceByKey, me quedo con solo una dupla por categoría con el total de vistas
# 4º Con el sortBy ordeno las categorías por nº de vistas 
# 5º Con first() me quedo con la dupla buscada: la ordenación por defecto es de menor a mayor)
menosVista = rdd2unido.filter(lambda x: len(x.split('\t'))>15).map(funcion1).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1]).first()

# Convierto la dupla en RDD para poder guardarlo. Lo siento, no he encontrado otra manera que usar el parallelize
menosVista=sc.parallelize([menosVista])

# guardamos la salida 
menosVista.saveAsTextFile(salida)

# detenemos el Spark session
spark.stop()