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
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


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


def menuDep():
    print("Seleccione el departamento que desea transportar")
    print("1. Departamento de Medios y Presentaciones")
    print("2. Departamento de Pinturas y Esculturas")
    print("3. Departamento de Fotografía")
    print("4. Departamento de Arquitectura y Diseño")
    print("5. Departamento de Impresiones y Dibujos")
    print("6. Departamento de Cine")
    print("7. Coleccion Fluxus")

catalog = None

def initCatalog(tipo):

    return controller.initCatalog(tipo)


def loadArtists(catalog):

     return controller.loadArtists(catalog)


def loadArtworks(catalog):

    return controller.loadArtworks(catalog)


def listarArtistas(catalog, inicio, fin):
    
    return controller.listarArtistas(catalog, inicio, fin)


def sortArtworksByDateAcquired(catalog, inicio, fin):

    return controller.sortArtworksByDateAcquired(catalog, inicio, fin)


def sortArtworksByCID(catalog, nombre):

    return controller.sortArtworksByCID(catalog, nombre)


def sortbyNationality(catalog):

    return controller.sortbyNationality(catalog)


def transportCost(catalog, department):
    
    return controller.transportCost(catalog, department)

"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 0:

        catalog = initCatalog("ARRAY_LIST")  

        loadArtists(catalog)
        loadArtworks(catalog)
         
        print("Artistas Cargados " + str(lt.size(catalog["artists"])))
        print("Artworks cargados " + str(lt.size(catalog["artworks"])))
        
        print("Últimos 3 Artistas")
        i = 2
        while i >= 0:
            print (str(lt.getElement((catalog["artists"]), lt.size(catalog["artists"])-i)))
            i-=1
        
        print("Ultimos 3 Artworks")
        j = 2
        while j >= 0:
            print (str(lt.getElement((catalog["artworks"]),lt.size(catalog["artworks"])-j)))
            j-=1
  

    elif int(inputs[0]) == 1:

        print("Digite las fechas inciales y finales a consultar")
        date1 = int(input("Año inicial: " ))
        date2 = int(input("Año final: " ))
        lista = listarArtistas(catalog, date1, date2)

        print("Hay ", lt.size(lista), "artistas en el rango de ", date1, "y ", date2)
        print("================================================================")
        print("Los primeros 3 y ultimos 3 artistas del rango son:")
        for i in range(1, lt.size(lista)):
            if i < 4:
                print("--------------------------------------------------------")
                print (lt.getElement(lista, i))     
        print("********************************************************")      
        for i in range (lt.size(lista)-3, lt.size(lista)):
            if i <= lt.size(lista):
                print("--------------------------------------------------------")
                print(lt.getElement(lista, i))

    elif int(inputs[0]) == 2:

        date1 = (input("Fecha inicial (YYYY-MM-DD): " ))
        date2 = (input("Fecha final (YYYY-MM-DD): " ))
        lista_ordenada = sortArtworksByDateAcquired(catalog, date1, date2)
        print("Hay ", lt.size(lista_ordenada), "artworks en el rango de ", date1, "y ", date2)
        print("================================================================")
        print("Los primeros 3 y ultimos 3 artworks del rango son:")
        for i in range(1, lt.size(lista_ordenada)):
            if i < 4:
                print("--------------------------------------------------------")
                print (lt.getElement(lista_ordenada, i))
        print("********************************************************") 
        for i in range (lt.size(lista_ordenada)-3, lt.size(lista_ordenada)):
            if i <= lt.size(lista_ordenada):
                print('--------------------------------------------------------')
                print(lt.getElement(lista_ordenada, i))

    elif int(inputs[0]) == 3:  

        nombre = input("Inserte el nombre del artista a consultar: " )
        obras_Artista = sortArtworksByCID(catalog, nombre)
        cantidadObras, tecnicas, tecnica_mas_usada, long, obras_tecnicaUsada = obras_Artista
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Informacion encontrada para al autor " + nombre)
        print("Cantidad obras :", cantidadObras)
        print("Tecnicas :", tecnicas)
        print("Tecnica mas usada :", tecnica_mas_usada)
        print("Obras con tecnica mas usada : " + str(long))
        print("Primeras 5 obras con esa tecnica")
        print("---------------------------------------------------------")
        j = 0
        for y in obras_tecnicaUsada:
            x =  str(y["Title"] + " // " + y["Date"] + " // " + y["Medium"] + " // " + y['Dimensions'])
            if j < 5:        
                print(x)
                print('---------------------------------------------------------')
                j+=1
    
    elif int(inputs[0])==4:

        sorted, aux_dict = sortbyNationality(catalog)
        print(lt.size(sorted))
        z = 0
        for nationality in aux_dict:
            if z<=9:
                print ("%-20s %4.1f" % (nationality, aux_dict[nationality]))
            z+=1
        i = 1
        while i < 4:
            print (str(lt.getElement(sorted, i)))
            i+=1
        
        print("Ultimos 3 Artworks")
        j = 2
        while j >= 0:
            print (str(lt.getElement(sorted,lt.size(sorted)-j)))
            j-=1
    elif int(inputs[0]) == 5:

        print ("Seleccione el departamento que desea transportar: \n")
        menuDep()
        inputDep = int(input())
        if inputDep==1:
            sorted, costo_total, total_obras = transportCost(catalog, "Media and Performance")
        elif inputDep==2:
            sorted, costo_total, total_obras = transportCost(catalog, "Painting & Sculpture")
        elif inputDep==3:
            sorted, costo_total, total_obras = transportCost(catalog, "Photography")
        elif inputDep==4:
            sorted, costo_total, total_obras = transportCost(catalog, "Architecture & Design")
        elif inputDep==5:
            sorted, costo_total, total_obras = transportCost(catalog, "Drawings & Prints")
        elif inputDep==6:
            sorted, costo_total, total_obras = transportCost(catalog, "Film")
        elif inputDep==7:
            sorted, costo_total, total_obras = transportCost(catalog, "Fluxus Collection")
            
        print("Se transportarán ", total_obras, "obras por un costo de ", round(costo_total, 2), "USD")
        for i in range(1, lt.size(sorted)):
            if i < 4:
                print("--------------------------------------------------------")
                print (lt.getElement(sorted, i))

    else:
        sys.exit(0)

sys.exit(0)
0