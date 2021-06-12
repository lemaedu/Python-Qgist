#importo la libreria
import os
#Mensaje que muestra al usuario
print("Ingrele la ruta en donde desea crear la carpeta")
#variable ruta almacena la ruta donde se va ha creat
ruta = input()

try:
    #Crea la carpeta principal
    os.mkdir(ruta)
    i = 1
    #Selecciono while por que me permite recorrer la variable i facilmente
    while i <=1000 :
        #en variable r de almacena la ruta y el nombre Subcarpeta adiciando el indice 
        r=ruta+"\Subcarpeta"+str(i)
        #crea la subcarpeta
        os.mkdir(r)
        i += 1 
except OSError:
    print("La creación del directorio %s falló" % ruta)
else:
    print("Se ha creado el directorio: %s " % ruta)
