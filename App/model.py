"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """



import config as cf
from datetime import date
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {"artists":None, 
               "artworks": None,
               "medium": None}


    catalog["artists"] = lt.newList("ARRAY_LIST")

    catalog["artworks"] = lt.newList("ARRAY_LIST")

    """
    Este indice crea un map cuya llave es la técnica
    """
    catalog["medium"] = mp.newMap(800,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMedium)
   

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):

    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog["artists"], artist)

def addArtwork(catalog, artwork):
    # Se adiciona la obra de arte a la lista de obras de arte
    lt.addLast(catalog["artworks"], artwork)
    mp.put(catalog["medium"], artwork["Medium"], artwork)
 



# ==============================
# Funciones de Comparacion
# ==============================
def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"]) < int(artist2["BeginDate"]))


def compareAlphabetically(artwork1, artwork2):

    return (str(artwork1["Title"]) < str(artwork2["Title"]))


def comparebyConsID(art1, art2):

    return (str(art1["ConstituentID"]) < str(art2["ConstituentID"]))


def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"]) < int(artist2["BeginDate"]))


def compareByCosts(art1,art2):

    return (int(art1["Cost"])>int(art2["Cost"]))


def compareMedium(artwork1, artwork2):
    
       return (str(artwork1) < str(artwork2))


def cmpArtWorkByDateAcquired(artwork1, artwork2):

    fecha1 = artwork1['DateAcquired']
    fecha2 = artwork2['DateAcquired']

    if fecha1 == "":
        fecha1 = '1700-01-01'
    if fecha2 == "": 
        fecha2 = '1700-01-01'

    dt1 = date.fromisoformat(fecha1)
    dt2 = date.fromisoformat(fecha2)

    return (dt1 < dt2)

def cmpArtworkbyYear (artw1,artw2):
    return artw1["Date"]<artw2["Date"]

def FindIDArtist(catalog, nombre):
    
    artistas = catalog["artists"]
    c = False
    while c == False:
        for i in range(lt.size(artistas)):
            x = lt.getElement(artistas, i)
            if x['DisplayName'] == nombre:
                IDArtista = x['ConstituentID']
                c = True
    
    return IDArtista


def contar_tecnicas(obrasArtista):

    tecnicas = lt.newList(datastructure="ARRAY_LIST")
    for i in range(lt.size(obrasArtista)):
        artwork = lt.getElement(obrasArtista, i)
        if lt.isPresent(tecnicas, artwork["Medium"]) == 0:
            lt.addLast(tecnicas, artwork["Medium"])
    tecnicas = lt.size(tecnicas)

    return tecnicas


def tecnica_mas_usada(obrasArtista):

    obras = obrasArtista["elements"]
    dic = {}
    for obra in range(len(obras)):

        iguales = 0
        #(obras[obra]["Medium"])
        for obra1 in range(len(obras)):
            if obras[obra]["Medium"] == obras[obra1]["Medium"]:
                iguales += 1   
        dic[obras[obra]["Medium"]] = iguales
    mayor = 0 
    obramayor = ""    
    for llave in dic:
        if dic[llave] > mayor:
           mayor = dic[llave]
           obramayor = llave
    letra = {obramayor:mayor} 

    return obramayor
     

def obras_tecnicaUsada(obrasArtista, obramayor):

    obrasA = obrasArtista["elements"]
    obras = lt.newList(datastructure='ARRAY_LIST')

    for i in range(len(obrasA)):
        if obrasA[i]["Medium"] == obramayor:
            lt.addLast(obras, obrasA[i])
    obrasTecnica = obras["elements"]
    long = len(obrasTecnica)

    return obrasTecnica, long

   
def listarArtistas(catalog, inicio, fin):

    ordenarArtistas(catalog["artists"])

    rango_artistas = lt.newList(datastructure="SINGLE_LINKED")

    i = 1
    c = False
    while i <= lt.size(catalog["artists"]) and not c:

        artista = lt.getElement(catalog["artists"], i)
        if int(artista["BeginDate"]) > fin:
            c = True
        
        if int(artista["BeginDate"]) >= inicio and int(artista["BeginDate"]) <= fin:
            lt.addLast(rango_artistas, artista)
        i+=1

    return rango_artistas

def ordenarArtistas(lista):
    
    return mg.sort(lista, compareBeginDate)
            

def sortArtworksByDateAcquired(catalog, inicio, fin):

    sub_list = lt.subList(catalog["artworks"], 1, (lt.size(catalog["artworks"])))
    sub_list = sub_list.copy()
    sorted = mg.sort(sub_list, cmpArtWorkByDateAcquired)

    rango_artworks = lt.newList(datastructure="SINGLE_LINKED")

    i = 1
    c = False
    while i<=lt.size(sorted) and not c:

        artwork = lt.getElement(sorted, i)
        if (artwork["DateAcquired"]) > fin:
            c = True
        
        if (artwork["DateAcquired"]) >= inicio and (artwork["DateAcquired"]) <= fin:
            lt.addLast(rango_artworks, artwork)
        i+=1

    return rango_artworks


def sortArtworksByCID(catalog, nombre):

    artworks = (catalog["artworks"])
    ID_Artista = FindIDArtist(catalog, nombre)
    obrasArtista = lt.newList(datastructure="ARRAY_LIST")
    for i in range(lt.size(artworks)):
        artwork = lt.getElement(artworks, i)
        if artwork['ConstituentID'][1:-1] == ID_Artista:
            lt.addLast(obrasArtista, artwork)
    cantidad_obras = lt.size(obrasArtista)
    tecnicas = contar_tecnicas(obrasArtista)
    obramayor = tecnica_mas_usada(obrasArtista)
    obras_tecnicaMasUsada, long = obras_tecnicaUsada(obrasArtista, obramayor)

    return cantidad_obras, tecnicas, obramayor, long, obras_tecnicaMasUsada


def sortByNacionality(catalog):

    artworks = lt.newList(datastructure="ARRAY_LIST")
    aux_dict = dict()
    contadora = 0
    i = 1

    while i<=lt.size(catalog["artworks"]):
        j = 1

        while j<=lt.size(catalog["artists"]):
            
            a = lt.getElement(catalog["artworks"], i)['ConstituentID'][1:-1]
            if ',' in a:
                for id in range(len(a.split(','))):
                    if id == 0: 
                        if a.split(',')[id] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                            contadora+=1
                            aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                            if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                                lt.addLast(artworks,lt.getElement(catalog["artworks"], i))
                    else:
                        if a.split(',')[id][1:] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                            contadora+=1
                            aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                            if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                                lt.addLast(artworks,lt.getElement(catalog["artworks"], i))
            else:
                if lt.getElement(catalog["artworks"], i)['ConstituentID'][1:-1] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                    contadora+=1
                    aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                    if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                         lt.addLast(artworks,lt.getElement(catalog["artworks"], i))  
            j+=1

        i+=1
    sorted = mg.sort(artworks, compareAlphabetically)

    return sorted, aux_dict


def transportRules(catalog, department):

    listawCosts = lt.newList("ARRAY_LIST")
    aw = catalog["artworks"]
    i = 1
    total_obras =  0
    costo_total = 0

    while i <= lt.size(aw):
        awactual = lt.getElement(aw, i)
        if awactual["Department"]==department :
            costo = 48
            total_obras += 1
            if awactual["Diameter (cm)"]!="":
                r = float(awactual["Diameter (cm)"])/200
                area = (math.pi)*(r)**2
                costo = area*72
            
            if awactual["Height (cm)"]!="" and awactual["Width (cm)"]!="":
                if awactual["Height (cm)"]!="0" and awactual["Width (cm)"]!="0":

                    h = float(awactual["Height (cm)"])/100
                    w = float(awactual["Width (cm)"])/100
                    area = h*w
                    costo = area*72

            if awactual["Depth (cm)"] !="" and awactual["Depth (cm)"] !="0":
                if i == 47:
                        print("")
                d = (float(awactual["Depth (cm)"]))/100
                h = (float(awactual["Height (cm)"]))/100
                w = (float(awactual["Width (cm)"]))/100
                if h == 0:
                    area = d * w
                    costo = area*72
                if w == 0:
                    area = d * h
                    costo = area*72
                vol = d*w*h
                costov = vol*72
                if costov > costo:
                    costo = costov

            if awactual["Weight (kg)"]!="":

                we = float(awactual["Weight (kg)"])
                costop = we * 72
                if costop > costo:
                    costo = costop
                if costop > costov:
                    costo = costop
                elif costov > costop:
                    costo = costov
            
            awactual["Cost"] = round(costo,2)

            if awactual["Cost"] == "0":
                awactual["Cost"] == 48
            
            costo_total += costo
            
            lt.addLast(listawCosts, awactual)
        i+=1

    sorted = mg.sort(listawCosts, compareByCosts)

    return sorted, costo_total, total_obras

def tecnica_mas_antigua(catalog, medio):

    listaTecnicas = mp.keySet(catalog["medium"])
    listaArtworks = mp.valueSet(catalog["medium"])
    listaFinal = lt.newList("ARRAY_LIST")

    i = 0

    while i<=mp.size(catalog["medium"]):

        if lt.getElement(listaTecnicas, i) == medio:
            artw = lt.getElement(listaArtworks, i)
            lt.addLast(listaFinal, artw)
        i+=1
    
    sorted = mg.sort(listaFinal, cmpArtworkbyYear)

    return(sorted["elements"])

