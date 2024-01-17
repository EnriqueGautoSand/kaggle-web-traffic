import pandas as pd
def guararDataframeToCSV(dataFrame,salidaCarpetaSTR,NombreArchivoCSV):
    """

    :param dataFrame: dataFrame
    :param salidaCarpetaSTR: nombre de la carpeta de salida
    :param NombreArchivoCSV: nombre del archivo csv de salida
    :return:
    """
    salidaCarpeta = salidaCarpetaSTR
    dataFrame.to_csv(salidaCarpeta + NombreArchivoCSV)  # guardo en csv

    dfPruebaSalida = pd.read_csv(salidaCarpeta + NombreArchivoCSV, index_col=0)

    # remover Columnas en cero
    for col in dfPruebaSalida.columns:
        # imprimo columnas con todos zeros para retirar columna
        print(col, (dfPruebaSalida[col] == 0).all())
        # columnas a retirar
        # Sesiones con conversiones True
        # Sesiones con transacciones True
        # Tráfico de pago True
        # dropeo columnas True con todo cero
        if (dfPruebaSalida[col] == 0).all():
            dfPruebaSalida = dfPruebaSalida.drop(col, axis=1)

    # dropeo columna 'unnamed'
    # dataFrame=dataFrame.drop(dataFrame.columns[dataFrame.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    #print(dfPruebaSalida.columns)

    # funcion remover Filas en cero // no lo uso mas porque antes habia muchas filas en cero al comienzo pero ya no
    #dfPruebaSalida = dfPruebaSalida.loc[(dfPruebaSalida != 0).any(axis=1)]

    print("Leyendo Salida")
    print(dfPruebaSalida.head())
    print(dfPruebaSalida.values)

    salidaCarpeta = salidaCarpetaSTR
    dfPruebaSalida.to_csv(salidaCarpeta + NombreArchivoCSV)