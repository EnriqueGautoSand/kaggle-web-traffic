import pandas as pd
from UA_dimensiones_promedios import agregar_columnas,Promedio_desvioEstandar
from paisUA import agregar_columnaPais
from guardarToCSV import guararDataframeToCSV
#ahora agragare agrupacion_canales
pd.set_option('display.max_columns', None)

analyticsUniversal="informe_UNaM_UA_2018-jun4_agrupacion_canales.csv"
dir="./datosDataStudio/"
dfAgrupacionCanales = pd.read_csv(dir+analyticsUniversal)
print('dfAgrupacionCanales')
print(dfAgrupacionCanales.head())
print(dfAgrupacionCanales.columns)
data = {'Fecha':[]}

dfAgrupacionCanales=agregar_columnas(dfAgrupacionCanales,'Agrupación de canales predeterminada', 'Número de vistas de página')
dfAgrupacionCanales=Promedio_desvioEstandar(dfAgrupacionCanales,'Agrupación de canales predeterminada')

#ahora agragare sistema operativo
analyticsUniversal="informe_UNaM_UA_2018-jun4_sistema_operativo.csv"
dfsisOperativo = pd.read_csv(dir+analyticsUniversal)
print('dfsisOperativo')
print(dfsisOperativo.columns)
print('pre',dfsisOperativo['Sistema operativo'].unique())

dfsisOperativo=agregar_columnas(dfsisOperativo,'Sistema operativo','Número de vistas de página')


asumar=['Samsung', 'Nokia', 'Playstation 4', 'Xbox','Sistema operativo (not set)']# sumo las vistas a not se
dfsisOperativo['Sistema operativo (not set)']=dfsisOperativo[asumar].sum(axis=1)
aborrar=['Samsung', 'Nokia', 'Playstation 4', 'Xbox']
dfsisOperativo = dfsisOperativo.drop(aborrar, axis=1)
print('post',dfsisOperativo.columns)
dfsisOperativo=Promedio_desvioEstandar(dfsisOperativo,'Sistema operativo')
print('post2',dfsisOperativo.columns)
print('head10',dfsisOperativo.head(10))

##

#    Pais

##
pd.set_option('display.max_columns', None)
analyticsUniversal="informe_UNaM_UA_2018-jun4_Pais.csv"
dir="./datosDataStudio/"
dfPais = pd.read_csv(dir+analyticsUniversal)
print(dfPais.head())
print(dfPais.columns)
dfPais=agregar_columnaPais(dfPais,'País','Número de vistas de página')

#categoria de dispositivo
analyticsUniversal="informe_UNaM_UA_2018-jun4_categoria_dispositivo.csv"
dir="./datosDataStudio/"
dfCategoriaDispositivo = pd.read_csv(dir+analyticsUniversal)
print(dfCategoriaDispositivo.columns)
dfCategoriaDispositivo=agregar_columnas(dfCategoriaDispositivo,'Categoría de dispositivo','Número de vistas de página')
dfCategoriaDispositivo=Promedio_desvioEstandar(dfCategoriaDispositivo,'Categoría de dispositivo')
print('head10',dfCategoriaDispositivo.head(10))

#totales
analyticsUniversalTotales="informe_UNaM_UA_totales_Tabla.csv"
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
NombreArchivoCSVSalida="UA2018SalidaUNaM.csv"
guararDataframeToCSV(dfUnion,salidaCarpeta,NombreArchivoCSVSalida)





