#Creando capas de puntos temporal
#Es recomendable crear una capa en memoria, para que el 
#usuario decida si desea guardar la capa

#Crear una capa de puntos
#Obtiente la capa activa

# se agrega cpas desde WMS http://www.geoportaligm.gob.ec/nacional/wms
capaActAeropuertos=iface.activeLayer()

#centro, capa aeropuerto
centroAeropuerto=capaAeropuertos.extent().center()

#Crea nueva capa
uri="point?crs=epsg:4326&field=id:integer"

capa=QgsVectorLayer(uri, "centro aeropuerto","memory")

#Creamos la entidad
entidad=QgsFeature()
entidad.setFields(capaActAeropuertos.fields())

#Creamos geometria
geometria=QgsGeometry.fromPointXY(centroAeropuerto)

#Ponemos capa en edicion con provider
capa.dataProvider().addAttributes(capaActAeropuertos.fields())

#Valida capa
capa.isValid()

entidad.setGeometry(geometria)

capa.dataProvider().addFeatures([entidad])

#instanciamos la capa
QgsProject.instance().addMapLayer(capa)
