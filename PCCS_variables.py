# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:45:27 2017

@author: carlos.arana
"""

'''
Descripcion:
Script para revisar variables existentes en un dataset.
El script revisa, a partir de una lista, si las variables se encuentran previamente identificadas
en el proyecto de la PCCS (En el archivo PCCS_variables.csv). Si la variable existe, le asigna la 
definición previamente establecida y almacena ambos valores en un diccionario.
Si no existe, pide la definición al usuario, la guarda en 'PCCS_variables.csv' y almacena la variable
y su descripción en un diccionario.
Regresa una Pandas.Series a partir del diccionario almacenado.
'''

# Librerias Utilizadas
import csv
import pandas

def variables(lista):
    archivovariablescsv = r'D:\PCCS\01_Analysis\01_DataAnalysis\00_Parametros\scripts\PCCS_variables\PCCS_variables.csv'
    with open(archivovariablescsv, 'r') as thefile:
        reader = csv.reader(thefile)
        dictvariables = {}
        for row in reader:
            if row == []: continue
            k, v = row
            dictvariables[k] = v

    # Creacion de nuevo diccionario para actualizar variables del archivo maestro
    actualizacion_variables = dictvariables

    actualizacion_variables['TIPO_SUN']
    # Diccionario para almacenar el metadato
    metavariables = {}

    for i in lista:
        if i in dictvariables.keys():
            print(i)
            metavariables[i] = dictvariables[i]
            continue
        else:
            hacer = input('La variable "{}" no existe en el proyecto. [A]gregar [S]alir:'.format(i)).upper()
            if hacer == 'S':
                raise ValueError('Script terminado por el usuario')
            elif hacer == 'A':
                valor = input('Escribe la descripcion para la variable "{}"'.format(i))
                actualizacion_variables[i] = valor
                metavariables[i] = dictvariables[i]
            else:
                raise ValueError('{} no es una accion valida'.format(hacer))

    with open(archivovariablescsv, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in actualizacion_variables.items():
            writer.writerow([key, value])

    return pandas.DataFrame.from_dict(metavariables, orient='index').rename(columns={0:'DESCRIPCION'})