#importa funciones
import processing

#Consultar algoritmo que se debe usuar

for alg in QgsApplication.processingRegistry().algorithms():
    if 'merge' in alg.id():
        print(alg.id())
 
 #Solo para consultar la herramiente       
processing.algorithmHelp("native:mergevectorlayers")
