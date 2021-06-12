import os
#instancia al proyecto por única vez
proyecto=QgsProject.instance()

#Path de capas
carpetaArchivos = r"C:\datosValle"
#agrega capas al mapLayer
iface.addVectorLayer(carpetaArchivos+"\gdb","mapas","ogr")

#crear capa
capa1=QgsVectorLayer(carpetaArchivos+"\gdb","","")
#asignar nombre a capa
capa1.setName("Capa 1")

#Adiciona capa al proyecto
proyecto.addMapLayer(capa1)


#capturar  layer/capas
iface.mapCanvas().layer(1).setName("capa1")
