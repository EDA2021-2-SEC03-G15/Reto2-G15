"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#########################   Menus   ################################

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Listar cronológicamente artistas")
    print("2- Listar cronológicamente artworks")
    print("3- Clasificar obras de un artista por técnica")
    print("4- Clasificar obras de un artista por nacionalidad")
    print("5- Transportar obras")
    print("6- Proponer exposicion")
    print("7- Salir")

##########################   Controller Functions   ###############################

def initCatalog():

    return controller.initCatalog()

def loadArtists(catalog):

     return controller.loadArtists(catalog)

def loadArtworks(catalog):

    return controller.loadArtworks(catalog)

def ordenarArtistasReq1(catalog, inicio, fin):

    return controller.ordenarArtistasReq1(catalog, inicio, fin)

def ordenarArtworksReq2(catalog, inicio, fin):

    return controller.ordenarArtworksReq2(catalog, inicio, fin)

def clasificarObrasNacionalidadReq4(catalog):

    return controller.clasificarObrasNacionalidadReq4(catalog)
def clasificarArtworksArtistaPorTecnica(catalog, nombre):
    
    return controller.clasificarArtworksArtistaPorTecnica(catalog, nombre)

###########################    Menu inputs and outputs   ######################################

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 0:

        print("Cargando información de los archivos ....")

        catalog = initCatalog()

        loadArtists(catalog)
        loadArtworks(catalog)
         
        print("Artistas Cargados " + str(lt.size(catalog["artists"])))
        print("Artworks cargados " + str(lt.size(catalog["artworks"])))
    
    elif int(inputs[0]) == 1:

        inicio = int(input("Inserte fecha inicial: "))
        final = int(input("Inserte fecha final: "))

        print("En el rango de fechas comprendido entre", inicio, "y", final, "se encuentran", 
                (ordenarArtistasReq1(catalog, inicio, final)), "artistas")
        print("========================================================")
        for elemento in (ordenarArtistasReq1(catalog, inicio, final))[0]:

            print(elemento)

    elif int(inputs[0]) == 2:

        inicio = input("Inserte fecha inicial (YYYY-MM-DD): ")
        final = input("Inserte fecha final (YYYY-MM-DD): ")
    
        for artwork in (ordenarArtworksReq2(catalog, inicio, final))[0]:

            print(artwork)
            print("========================================================")
    
    elif int(inputs[0]) == 4:

        clasificarObrasNacionalidadReq4(catalog)
        

    elif int(inputs[0]) == 3:

        nombre = input("Inserte el nombre del artista a consultar: " )
        obras_Artista = clasificarArtworksArtistaPorTecnica(catalog, nombre)
        cantidadObras, tecnicas, tecnica_mas_usada, longitud, obras_tecnicaUsada = obras_Artista
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Informacion encontrada para al autor " + nombre)
        print("Cantidad obras :", cantidadObras)
        print("Tecnicas :", tecnicas)
        print("Tecnica mas usada :", tecnica_mas_usada)
        print("Obras con tecnica mas usada : " + str(longitud))
        print("Primeras 5 obras con esa tecnica")
        print("---------------------------------------------------------")
        j = 0
        for y in obras_tecnicaUsada:
            x =  str(y["Title"] + " // " + y["Date"] + " // " + y["Medium"] + " // " + y['Dimensions'])
            if j < 5:        
                print(x)
                print('---------------------------------------------------------')
                j+=1
sys.exit(0)
