import pandas as pd
from UA_dimensiones_promedios import agregar_columnas,Promedio_desvioEstandar
from paisUA import agregar_columnaPais
from guardarToCSV import guararDataframeToCSV
#ahora agragare agrupacion_canales
pd.set_option('display.max_columns', None)

analyticsUniversal="editorialUniversitaria_UA_2018-oct4_AgrupacionCanales.csv"
dir="./datosDataStudio/"
dfAgrupacionCanales = pd.read_csv(dir+analyticsUniversal)

print(dfAgrupacionCanales.head())
data = {'Fecha':[]}
print(dfAgrupacionCanales.columns)
dfAgrupacionCanales=agregar_columnas(dfAgrupacionCanales,'Agrupación de canales predeterminada', 'Número de vistas de página')
asumar=['Paid Search','Direct']# sumo las vistas
dfAgrupacionCanales['Direct']=dfAgrupacionCanales[asumar].sum(axis=1)# sumo las vistas
aborrar=['Paid Search']
dfAgrupacionCanales = dfAgrupacionCanales.drop(aborrar, axis=1)# borro columnas
dfAgrupacionCanales=Promedio_desvioEstandar(dfAgrupacionCanales,'Agrupación de canales predeterminada')
print('head10 dfAgrupacionCanales',dfAgrupacionCanales.head(10))


#ahora agragare sistema operativo
analyticsUniversal="editorialUniversitaria_UA_2018-oct4_SO.csv"
dfsisOperativo = pd.read_csv(dir+analyticsUniversal)
print(dfsisOperativo.columns)
dfsisOperativo=agregar_columnas(dfsisOperativo,'Sistema operativo','Número de vistas de página')
print(dfsisOperativo['Sistema operativo (not set)'].unique())
asumar=['Playstation 4', 'FreeBSD','Sistema operativo (not set)']# sumo las vistas
dfsisOperativo['Sistema operativo (not set)']=dfsisOperativo[asumar].sum(axis=1)
aborrar=['Playstation 4', 'FreeBSD']
dfsisOperativo = dfsisOperativo.drop(aborrar, axis=1)# borro columnas

dfsisOperativo=Promedio_desvioEstandar(dfsisOperativo,'Sistema operativo')
print('head10',dfsisOperativo.head(10))

##

#    Pais

##
pd.set_option('display.max_columns', None)
analyticsUniversal="editorialUniversitaria_UA_2018-oct4_Pais.csv"
dir="./datosDataStudio/"
dfPais = pd.read_csv(dir+analyticsUniversal)
print(dfPais.head())
print(dfPais.columns)
dfPais=agregar_columnaPais(dfPais,'País','Número de vistas de página')

#categoria de dispositivo
analyticsUniversal="editorialUniversitaria_UA_2018-oct4_catDispositivo.csv"
dir="./datosDataStudio/"
dfCategoriaDispositivo = pd.read_csv(dir+analyticsUniversal)
print(dfCategoriaDispositivo.columns)
dfCategoriaDispositivo=agregar_columnas(dfCategoriaDispositivo,'Categoría de dispositivo','Número de vistas de página')
dfCategoriaDispositivo=Promedio_desvioEstandar(dfCategoriaDispositivo,'Categoría de dispositivo')
print('head10',dfCategoriaDispositivo.head(10))

#totales
analyticsUniversalTotales="editorialUniversitaria_UA_2018-oct4_totales.csv"
dir="./datosDataStudio/"
dfTotales = pd.read_csv(dir+analyticsUniversalTotales)
print(dfCategoriaDispositivo.columns,dfTotales.head() )


#unir los dataframes en columnas
aUnir=[dfTotales,dfPais,dfCategoriaDispositivo,dfsisOperativo,dfAgrupacionCanales]
print('largo datasets')
for i in aUnir:
    print(i.shape)
dfUnion=pd.concat(aUnir,axis=1)

#guradamos a csv
salidaCarpeta="./salida/"
NombreArchivoCSVSalida="UA2018SalidaEditorialUniversitaria.csv"
guararDataframeToCSV(dfUnion,salidaCarpeta,NombreArchivoCSVSalida)





