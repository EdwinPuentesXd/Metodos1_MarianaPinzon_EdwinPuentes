# -*- coding: utf-8 -*-
"""
@author: EdwinXd
"""

"""parte 4"""
import pandas as pd
import matplotlib.pyplot as plt

def maximos_locales(name:str):
    lista=[]
    archivo=open(name, "r")
    linea=archivo.readline()
    while len(linea)!=0:
        datos= linea.replace("\n", "").split()
        columna=(float(datos[0]),float(datos[1]))
        lista.append(columna)
        linea=archivo.readline()
    maximuns = []
    for i in range(1, len(lista) - 1):
        if (lista[i][1] > lista[i - 1][1]) and (lista[i][1] > lista[i + 1][1]):
            maximuns.append(lista[i])
    columnas=["x","y"]
    dt_lista= pd.DataFrame(lista, columns=columnas)
    dt_maximuns= pd.DataFrame(maximuns, columns=columnas)
    return dt_lista,dt_maximuns

def visor(datos,datos2):
    plt.figure()
    subplot= datos.plot("x","y", legend=None)
    datos2.plot(kind="scatter", x="x",y="y", color="r", marker="o", ax=subplot)
    plt.show()
    
x,d=maximos_locales("EstrellaEspectro.txt")
visor(x,d)
