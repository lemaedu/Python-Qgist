#Este archivo captura el centro de las tres capas
def linea_centros():
    #obtiene la capa activa
    aeropuertos=iface.activeLayer()
    lagunas=iface.mapCanvas().layer(1)
    provincias=iface.mapCanvas().layer(3)
    #guarda en una lista los puntos centros de las capas
    puntosc=[aeropuertos.extent().center(),lagunas.extent().center(), provincias.extent().center()]
    
    #Crea capa1 de lineas
    uri="linestring?crs=epsg:4326&field=id:integer"
    #QgsVectorLayer(tipodecapa,"nombre de capa", en memoria)
    capal=QgsVectorLayer(uri,"Linea_centro", "memory")
    
    #definimos campos, para lo cual la capa debe estar como editable=dataProvider
    capal.dataProvider().addAttributes(aeropuertos.fields())
    
    #actualiza capa
    capal.updateFields()
    
    #creamos entidades o features
    entidad=QgsFeature()
    entidad.setFields(capal.fields())
    
    #creamos la geometria
    geom=QgsGeometry.fromPolylineXY(puntosc)
    
    entidad.setGeometry(geom)
    
    capal.dataProvider().addFeatures([entidad])
    
    #instanciar al proyecto
    QgsProject.instance().addMapLayer(capal)

#Este archivo captura el centro de las tres capas
#es una actualización del metodo linea_centros()
def poligono_centros():
    #obtiene la capa activa
    aeropuertos=iface.activeLayer()
    lagunas=iface.mapCanvas().layer(1)
    provincias=iface.mapCanvas().layer(3)
    #guarda en una lista los puntos centros de las capas
    puntosc=[aeropuertos.extent().center(),lagunas.extent().center(), provincias.extent().center()]
    
    #Crea capa1 de lineas
    uri="polygon?crs=epsg:4326&field=id:integer"
    #QgsVectorLayer(tipodecapa,"nombre de capa", en memoria)
    capal=QgsVectorLayer(uri,"poligono_centro", "memory")
    
    #definimos campos, para lo cual la capa debe estar como editable=dataProvider
    capal.dataProvider().addAttributes(aeropuertos.fields())
    
    #actualiza capa
    capal.updateFields()
    
    #creamos entidades o features
    entidad=QgsFeature()
    entidad.setFields(capal.fields())
    
    #creamos la geometria, para los polígonos debe estar en doble lista
    geom=QgsGeometry.fromPolygonXY([puntosc])
    
    entidad.setGeometry(geom)
    
    capal.dataProvider().addFeatures([entidad])
    
    #instanciar al proyecto
    QgsProject.instance().addMapLayer(capal)
    
#llama a la funcion
#linea_centros()
poligono_centros()