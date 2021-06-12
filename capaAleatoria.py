import random

def crear_capa(n):
    layer = QgsVectorLayer("Point?crs=EPSG:4326","capa","memory")
    layer.dataProvider().addAttributes([QgsField("id", QVariant.Int)])
    layer.updateFields()
    entidades = [] 
    for i in range(n):
        entidad = QgsFeature()
        entidad.setFields(layer.fields())
        x = random.uniform(-180,180)
        y = random.uniform(-90,90)
        pt = QgsPointXY(x,y)
        geom = QgsGeometry.fromPointXY(pt)
        entidad.setGeometry(geom)
        entidad.setAttribute(0,i)
        entidades.append(entidad)
        
    layer.dataProvider().addFeatures(entidades)
    return layer
    
capaAleatoria = crear_capa(50)
QgsProject.instance().addMapLayer(capaAleatoria)