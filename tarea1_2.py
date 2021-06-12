import os
path=os.lisdir(r'C:\datosValle')
print(path)

#declara variable
diccionarioPaises= {
    'Ecuador':'http://www.geoportaligm.gob.ec/nacional/wms?&request=GetCapabilities',
    'Peru':'https://www.idep.gob.pe/geoportal/services/DATOS_GEOESPACIALES/L%C3%8DMITES/MapServer/WMSServer?request=GetCapabilities&service=WMS',
    'COLOMBIA':'https://gw-geoportal-test.igac.gov.co/geoservices/geodesia/wfs?version=2.0.0&request=GetCapabilities' }
print(diccionarioPaises['Peru'])