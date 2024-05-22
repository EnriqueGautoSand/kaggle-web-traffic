import pandas as pd



#print(df['Agrupación de canales predeterminada'].unique())
def agregar_columnas(dataframe,dimension,objetivo):
    """

    :param dataframe: dataframe del csv
    :param dimension: dimension de google analytics en data studio looker
    :return: dataframe con los tag de dimension como columnas individuales
    """
    data = {}#este dic va a ser mi nuevo dataset
    lista_tags_unicos= dataframe[dimension].unique()

    for idx, nueva_columna in enumerate(lista_tags_unicos):
        if nueva_columna == '(not set)':
            data[dimension+' '+nueva_columna]=[]
            lista_tags_unicos[idx]=dimension+' '+nueva_columna
        else:
            data[nueva_columna] = []
    print('lista_tags_unicos',lista_tags_unicos)
    fechaAnterior = 0
    categorias = {}

    for ix, row in dataframe.iterrows():
        if fechaAnterior != 0:
            if row['Fecha'] != fechaAnterior:
                for cat in lista_tags_unicos:
                    if cat not in categorias:
                        data[cat].append(0)
                categorias = {}


        for j in lista_tags_unicos:
            comparacion=row[dimension]
            if comparacion=='(not set)':
                comparacion=dimension+' '+'(not set)'
                print('comparacion',comparacion)
                #data[j].append(row[objetivo])
                #break
            if comparacion == j:
                categorias[j] = 0
                data[j].append(row[objetivo])

                break

        fechaAnterior = row['Fecha']
    for cat in lista_tags_unicos:
        if cat not in categorias:
            data[cat].append(0)
    for key in data:
        print(key, len(data[key]))
    dataFrame = pd.DataFrame(data)
    print(dataFrame)
    return dataFrame

def Promedio_desvioEstandar(dataframe,dimension):
    promedio_Fila = dataframe.mean(axis=1)
    dataframe[dimension+' promedio'] = promedio_Fila#agrego promedio por fila al dataset
    desvioEstandar_Fila = dataframe.std(axis=1)
    dataframe[dimension+' std'] = desvioEstandar_Fila#agrego desvio estandar por fila al dataset
    return  dataframe




