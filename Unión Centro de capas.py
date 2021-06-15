#función que permite unir centros de capas visibles como lineas puntos y linesa
def union_centros():
    can=iface.mapCanvas()
    
    #listamos las capas visibles
    listaCapas=can.layers()
    
    #captura error en caso que no existiera capas visibles
    if len(listaCapas)<2:
        print("Error")
    else:
        sc=QgsProject.instance().crs().authid()
        #para trabajar con sistemas de coordenadas en la 
        #primera capa
        #sc=listaCapas[0].crs().authid()
        
        tf="&field=id:integer"
        
        #crea lista de puntos
        listac=[]
        for capa in listaCapas:
            listac.append(capa.extent().center())
        
        #CAPA DE LINEAS
        uril="linestring?crs="+sc+tf
        #QgsVectorLayer(tipodecapa,"nombre de capa", en memoria)
        capaLinea=QgsVectorLayer(uril,"Linea centro", "memory")
        
        #definimos campos, para lo cual la capa debe estar como editable=dataProvider
        capaLinea.dataProvider().addAttributes(listaCapas[0].fields())
        
        #actualiza capa
        capaLinea.updateFields()
        
        #creamos entidades o features
        entidadLinea=QgsFeature()
        entidadLinea.setFields(capaLinea.fields())
        
        #creamos la geometria
        geomLinea=QgsGeometry.fromPolylineXY(listac)        
        entidadLinea.setGeometry(geomLinea)        
        capaLinea.dataProvider().addFeatures([entidadLinea])
        
        #CAPA DE POLIGONOS        
        urip="polygon?crs="+sc+tf
        #QgsVectorLayer(tipodecapa,"nombre de capa", en memoria)
        capaPolg=QgsVectorLayer(urip,"Poligono centro", "memory")
        #definimos campos, para lo cual la capa debe estar como editable=dataProvider
        capaPolg.dataProvider().addAttributes(listaCapas[0].fields())
        #actualiza capa
        capaPolg.updateFields()
        #creamos entidades o features
        entidadPolg=QgsFeature()
        entidadPolg.setFields(capaPolg.fields())
        
        #creamos la geometria
        geomPolg=QgsGeometry.fromPolygonXY([listac])        
        entidadPolg.setGeometry(geomPolg)        
        capaPolg.dataProvider().addFeatures([entidadPolg])
        
        QgsProject.instance().addMapLayers([capaLinea,capaPolg])
        
union_centros()