import pandas as pd
from UA_dimensiones_promedios import agregar_columnas,Promedio_desvioEstandar
from paisUA import agregar_columnaPais
from guardarToCSV import guararDataframeToCSV
#ahora agragare agrupacion_canales
pd.set_option('display.max_columns', None)

analyticsGA4="Tum Transmedia GA4 grupo de canales predeterminado.csv"
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
dfAgrupacionCanales=Promedio_desvioEstandar(dfAgrupacionCanales,'Agrupación de canales predeterminada')

#ahora agragare sistema operativo
analyticsUniversal="Tum Transmedia GA4 SO.csv"
dfsisOperativo = pd.read_csv(dir+analyticsUniversal)
print('dfsisOperativo',dfsisOperativo.columns)
#['Fecha', 'Sistema operativo', 'Vistas']
dfsisOperativo.rename(columns = {'Fecha':'Fecha',
                            'Vistas':'Número de vistas de página'}, inplace = True)
dfsisOperativo=agregar_columnas(dfsisOperativo,'Sistema operativo','Número de vistas de página')
print(dfsisOperativo['Sistema operativo (not set)'].unique())
dfsisOperativo=Promedio_desvioEstandar(dfsisOperativo,'Sistema operativo')
print('head10',dfsisOperativo.head(10))

##

#    Pais

##
pd.set_option('display.max_columns', None)
analyticsGA="GA4_to_csv_ jun14_to_15may2023.csv"
analyticsUniversal="Tum Transmedia GA4 tabla pais.csv"
dir="./datosDataStudio/"
dfPais = pd.read_csv(dir+analyticsUniversal)
print(dfPais.head())
print('dfPais',dfPais.columns)
#'Fecha', 'País', 'Vistas'
dfPais.rename(columns = {'Vistas':'Número de vistas de página'}, inplace = True)
dfPais=agregar_columnaPais(dfPais,'País','Número de vistas de página')

#categoria de dispositivo
analyticsUniversal="Tum Transmedia GA4 categoria dispositivo.csv"
dir="./datosDataStudio/"
dfCategoriaDispositivo = pd.read_csv(dir+analyticsUniversal)
print('dfCategoriaDispositivo',dfCategoriaDispositivo.columns)
#'Fecha', 'Categoría de dispositivo', 'Vistas'
dfCategoriaDispositivo.rename(columns = {'Vistas':'Número de vistas de página'}, inplace = True)
dfCategoriaDispositivo=agregar_columnas(dfCategoriaDispositivo,'Categoría de dispositivo','Número de vistas de página')
dfCategoriaDispositivo=Promedio_desvioEstandar(dfCategoriaDispositivo,'Categoría de dispositivo')
print('head10',dfCategoriaDispositivo.head(10))

#totales
analyticsUniversalTotales="Tum Transmedia GA4 totales.csv"
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
NombreArchivoCSVSalida="TUMGA4Salida14Jun2022.csv"
guararDataframeToCSV(dfUnion,salidaCarpeta,NombreArchivoCSVSalida)





