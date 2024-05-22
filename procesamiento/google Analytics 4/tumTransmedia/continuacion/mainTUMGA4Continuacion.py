import pandas as pd
from UA_dimensiones_promedios import agregar_columnas,Promedio_desvioEstandar
from paisUA import agregar_columnaPais
from guardarToCSV import guararDataframeToCSV
#ahora agragare agrupacion_canales
pd.set_option('display.max_columns', None)

analyticsGA4="Tum Transmedia GA4_Agrupacion de canales.csv"
dir="./datosDataStudio/"
dfAgrupacionCanales = pd.read_csv(dir+analyticsGA4)

print(dfAgrupacionCanales.head())
print('dfAgrupacionCanales',dfAgrupacionCanales.columns)
#GA4'Fecha', 'Grupo de canales predeterminado de la sesión', 'Vistas'
dfAgrupacionCanales.rename(columns = {'Fecha':'Fecha',
                              'Grupo de canales predeterminado de la sesión':'Agrupación de canales predeterminada',
                              'Vistas':'Número de vistas de página'}, inplace = True)
data = {'Fecha':[]}
print(dfAgrupacionCanales.columns)
dfAgrupacionCanales=agregar_columnas(dfAgrupacionCanales,'Agrupación de canales predeterminada', 'Número de vistas de página')

asumar=['Organic Video','Organic Social']# sumo las vistas
dfAgrupacionCanales['Organic Social']=dfAgrupacionCanales[asumar].sum(axis=1)# sumo las vistas
asumar=['Unassigned','Direct']# sumo las vistas
dfAgrupacionCanales['Direct']=dfAgrupacionCanales[asumar].sum(axis=1)# sumo las vistas
aborrar=['Organic Video','Unassigned']
dfAgrupacionCanales = dfAgrupacionCanales.drop(aborrar, axis=1)# borro columnas

dfAgrupacionCanales=Promedio_desvioEstandar(dfAgrupacionCanales,'Agrupación de canales predeterminada')
print('head10 dfAgrupacionCanales',dfAgrupacionCanales.head(10))

#ahora agragare sistema operativo
analyticsUniversal="Tum Transmedia GA4_SO.csv"
dfsisOperativo = pd.read_csv(dir+analyticsUniversal)
print('dfsisOperativo',dfsisOperativo.columns)
#['Fecha', 'Sistema operativo', 'Vistas']
dfsisOperativo.rename(columns = {'Fecha':'Fecha',
                            'Vistas':'Número de vistas de página'}, inplace = True)
dfsisOperativo=agregar_columnas(dfsisOperativo,'Sistema operativo','Número de vistas de página')
#2024 - 15 -1
#print(dfsisOperativo['Sistema operativo (not set)'].unique())
asumar=['SymbianOS']#['Playstation 4']#,'Sistema operativo (not set)']# sumo las vistas a not se
dfsisOperativo['Sistema operativo (not set)']=dfsisOperativo[asumar].sum(axis=1)
aborrar=['SymbianOS']
dfsisOperativo = dfsisOperativo.drop(aborrar, axis=1)
dfsisOperativo['Chrome OS']=0
dfsisOperativo=Promedio_desvioEstandar(dfsisOperativo,'Sistema operativo')
print('head10',dfsisOperativo.head(10))

##

#    Pais

##
pd.set_option('display.max_columns', None)
analyticsUniversal="Tum Transmedia GA4_tabla pais.csv"
dir="./datosDataStudio/"
dfPais = pd.read_csv(dir+analyticsUniversal)
print(dfPais.head())
print('dfPais',dfPais.columns)
#'Fecha', 'País', 'Vistas'
dfPais.rename(columns = {'Vistas':'Número de vistas de página'}, inplace = True)
dfPais=agregar_columnaPais(dfPais,'País','Número de vistas de página')

#categoria de dispositivo
analyticsUniversal="Tum Transmedia GA4_Categoria de dispositivo.csv"
dir="./datosDataStudio/"
dfCategoriaDispositivo = pd.read_csv(dir+analyticsUniversal)
print('dfCategoriaDispositivo',dfCategoriaDispositivo.columns)
#'Fecha', 'Categoría de dispositivo', 'Vistas'
dfCategoriaDispositivo.rename(columns = {'Vistas':'Número de vistas de página'}, inplace = True)
dfCategoriaDispositivo=agregar_columnas(dfCategoriaDispositivo,'Categoría de dispositivo','Número de vistas de página')
print('dfCategoriaDispositivo cols',dfCategoriaDispositivo.columns)
#asumar=['desktop']#['smart tv','desktop']# sumo las vistas a not se
#dfCategoriaDispositivo['desktop']=dfCategoriaDispositivo[asumar].sum(axis=1)
#aborrar=['smart tv']
#dfCategoriaDispositivo = dfCategoriaDispositivo.drop(aborrar, axis=1)
dfCategoriaDispositivo=Promedio_desvioEstandar(dfCategoriaDispositivo,'Categoría de dispositivo')
print('head10',dfCategoriaDispositivo.head(10))

#totales
analyticsUniversalTotales="Tum Transmedia GA4_Totales.csv"
dir="./datosDataStudio/"
dfTotales = pd.read_csv(dir+analyticsUniversalTotales)
dfTotales.rename(columns = {'Vistas':'Número de vistas de página',
                                         'Sesiones por usuario':'Número de sesiones por usuario',
                                         'Total de usuarios':'Usuarios',
                                         }, inplace = True)
print(dfCategoriaDispositivo.columns,dfTotales.head() )


#unir los dataframes en columnas
aUnir=[dfTotales,dfPais,dfCategoriaDispositivo,dfsisOperativo,dfAgrupacionCanales]
print('largo datasets')
for i in aUnir:
    print(i.shape)
dfUnion=pd.concat(aUnir,axis=1)
print('dfUnion Columnas')
dfUnion.rename(columns = {'Organic Social':'Socials'}, inplace = True)

print(dfUnion.columns)
#guradamos a csv
salidaCarpeta="./salida/"
NombreArchivoCSVSalida="TUMGA4Salida14Jun2022Continuacion.csv"
guararDataframeToCSV(dfUnion,salidaCarpeta,NombreArchivoCSVSalida)





