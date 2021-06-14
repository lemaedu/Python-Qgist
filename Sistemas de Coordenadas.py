#Sistemas de coordenadas
#Se debe realizar con una capa activa
capaAaeropuertos=iface.activeLayer()

#instanciar al proyecto
proyecto=QgsProject.instance()
capaAaeropuertos.crs()
#indica el sistema de coordenadas
capaAaeropuertos.crs().authid()

#metodos para consultar sistema de coordenadas del proyecto
proyecto.crs()
proyecto.crs().authid()
proyecto.crs().toProj4()