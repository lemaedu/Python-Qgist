import processing
#variable que almavena la capa ferrocarriles
cap_ferr = r"C:\shape\ferrocarril\ferrocarril.shp"
#variable que almacena la capa vias
cap_vias = r"C:\shape\vias\vias.shp"
#Dirección donde se almacenara el resultado
cap_res =r"C:\shape\resultado\resultado.shp"
parameters = {'LAYERS':[cap_ferr,cap_vias],'CRS':'EPSG:4326','OUTPUT':cap_res}
feedback = QgsProcessingFeedback()
processing.runAndLoadResults('native:mergevectorlayers',parameters,feedback=feedback)