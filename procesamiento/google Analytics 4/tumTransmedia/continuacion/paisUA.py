import pandas as pd



def agregar_columnaPais(dataframe,dimension,objetivo):
    """

    :param dataframe: dataframe del csv
    :param dimension: dimension de google analytics en data studio looker
    :param objetivo: columna a copiar los datos
    :return: dataframe con los tag de dimension como columnas individuales
    """
    data = {}#este dic va a ser mi nuevo dataset
    lista_tags_unicos= ['Argentina','Otros Paises']

    for idx, nueva_columna in enumerate(lista_tags_unicos):
        data[nueva_columna] = []
    print('lista_tags_unicos',lista_tags_unicos)
    fechaAnterior = 0
    categorias = {}
    sumarOtrosPaises = 0
    for ix, row in dataframe.iterrows():
        if fechaAnterior != 0:
            if row['Fecha'] != fechaAnterior:
                for cat in lista_tags_unicos:
                    if cat not in categorias:
                        data[cat].append(0)
                    if cat=='Otros Paises' and cat in categorias:
                        data['Otros Paises'].append(sumarOtrosPaises)
                        sumarOtrosPaises = 0
                categorias = {}

        comparacion=row[dimension]
        if comparacion!='Argentina':
            comparacion='Otros Paises'
            sumarOtrosPaises += row[objetivo]
            categorias[comparacion] = 0

        if comparacion == 'Argentina': #si es argentina
            categorias[comparacion] = 0
            data[comparacion].append(row[objetivo])




        fechaAnterior = row['Fecha']
    for cat in lista_tags_unicos:
        if cat not in categorias:
            data[cat].append(0)
        if cat == 'Otros Paises' and cat in categorias:
            data['Otros Paises'].append(sumarOtrosPaises)
            sumarOtrosPaises = 0
    for key in data:
        print(key, len(data[key]))
    dataFrame = pd.DataFrame(data)
    print(dataFrame)
    return dataFrame
