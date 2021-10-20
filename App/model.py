
import config as cf
from datetime import date
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import csv
import math

##########################  Catalog  ######################################
def newCatalog():

    catalog = {"artists":None,
                "artworks": None,
                "begindate": None,
                "dateacquired": None,
                "medium": None,
                "nationality": None,
                "constituentid": None}

    catalog["artists"] = lt.newList("ARRAY_LIST")

    catalog["artworks"] = lt.newList("ARRAY_LIST")

    catalog["begindate"] = mp.newMap(360,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=None)

    catalog["dateacquired"] = mp.newMap(800,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=None)
    
    catalog["medium"] = mp.newMap(800,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=None)

    catalog["nationality"] = mp.newMap(2000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=None)

    catalog["constituentid"] = mp.newMap(800,
                            maptype='PROBING',
                            loadfactor=0.5,
                            comparefunction=None)

    return catalog

def addArtist(catalog, artist):

    lt.addLast(catalog["artists"], artist)
    mp.put(catalog["begindate"], artist["BeginDate"], artist)

def addArtwork(catalog, artwork):

    lt.addLast(catalog["artworks"], artwork)
    mp.put(catalog["dateacquired"], artwork["DateAcquired"],artwork)

#########################     Load Functions     ##########################################

def loadArtworks(catalog):

    artworksfiles = cf.data_dir + "Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    for artwork in input_file:
        addArtwork(catalog, artwork)

def loadArtists(catalog):

    artistsfiles = cf.data_dir + "Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistsfiles, encoding="utf-8"))
    for artist in input_file:
        addArtist(catalog, artist)
    
###############################    Requirements   #######################################

def ordenarArtistasReq1(catalog, inicio, fin):

    listabd = mp.keySet(catalog["begindate"])
    listaartistas = mp.valueSet(catalog["begindate"])
    listafinal = lt.newList("ARRAY_LIST")

    i = 0
    while i < lt.size(listabd):

        if int(lt.getElement(listabd, i)) >= inicio and int(lt.getElement(listabd, i)) <= fin:
           lt.addLast(listafinal, lt.getElement(listaartistas,i))
        i+=1

    sorted = mg.sort(listafinal, compareBeginDate)
    
    resultado = lt.newList("ARRAY_LIST")

    for j in range (1, lt.size(sorted)):

        a = lt.getElement(sorted, j)

        if (j<=3):

            lt.addLast(resultado, a)
        
        if (j>=(lt.size(sorted)-3)):

            lt.addLast(resultado, a)

    return (resultado["elements"], lt.size(sorted))

def ordenarArtworksReq2(catalog, fechainicial, fechafinal):

    listaadq = mp.valueSet(catalog["dateacquired"])
    
    sorted = mg.sort(listaadq, cmpArtWorkByDateAcquired)

    listafinal = lt.newList("ARRAY_LIST")

    for i in range(0, lt.size(sorted)):

        artwork = lt.getElement(sorted, i)
        if ((artwork["DateAcquired"]>fechainicial) == True) and ((artwork["DateAcquired"]<fechafinal) == True):

            lt.addLast(listafinal, artwork)

    tamaño = lt.size(listafinal)

    return (listafinal["elements"], tamaño)

###############################################################################################

def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"]) < int(artist2["BeginDate"]))

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