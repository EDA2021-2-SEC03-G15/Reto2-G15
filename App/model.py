
import config as cf
from datetime import date
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapstructure as mpa
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

<<<<<<< HEAD
    catalog["nationality"] = mp.newMap(100,
=======
    catalog["nationality"] = mp.newMap(200,
>>>>>>> fe62dcd259a818b0427c5929d815cc87facbe7ff
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=None)

    catalog["objectid"] = mp.newMap(800,
                            maptype='PROBING',
                            loadfactor=0.5,
                            comparefunction=None)

    catalog["constituentid"] = mp.newMap(800,
                            maptype='CHAINING',
                            loadfactor=0.5,
                            comparefunction=None)


    return catalog

def addArtist(catalog, artist):

    lt.addLast(catalog["artists"], artist)
    mp.put(catalog["begindate"], artist["BeginDate"], artist)
    mp.put(catalog["nationality"], artist["Nationality"], artist)
    mp.put(catalog["constituentid"], artist["ConstituentID"], artist)

def addArtwork(catalog, artwork):

    lt.addLast(catalog["artworks"], artwork)
<<<<<<< HEAD
    mp.put(catalog["dateacquired"], artwork ["DateAcquired"],artwork)
    mp.put(catalog["objectid"], artwork["ObjectID"], artwork)

=======
    mp.put(catalog["dateacquired"], artwork["DateAcquired"],artwork)
    mp.put(catalog["constituentid"], artwork["ConstituentID"][1:-1], artwork)
>>>>>>> fe62dcd259a818b0427c5929d815cc87facbe7ff

#########################     Load Functions     ##########################################

def loadArtworks(catalog):

    artworksfiles = cf.data_dir + "Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    c=0
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

    resultado = lt.newList("ARRAY_LIST")

    for j in range (1, lt.size(listafinal)):

        a = lt.getElement(listafinal, j)

        if (j<=3):

            lt.addLast(resultado, a)
        
        if (j>=(lt.size(listafinal)-3)):

            lt.addLast(resultado, a)

    return (resultado["elements"], tamaño)

def clasificarObrasNacionalidadReq4(catalog):

    artistas = mp.valueSet(catalog["constituentid"])
    consid = mp.keySet(catalog["constituentid"])
    artw = mp.valueSet(catalog["objectid"])

 
    infoArtistas = mp.newMap(800,
                            maptype='PROBING',
                            loadfactor=0.5,
                            comparefunction=None)
    i=0
    while i<lt.size(artw):

        cid1 = lt.getElement(artistas, i)["ConstituentID"]
        ar = lt.getElement(artistas, i)
        aw = lt.getElement(artw, i)
        awsp = str(aw["ConstituentID"][1:-1])
        if ',' in awsp:
            for id in (awsp).split(','):
                if cid1 in id.replace(" ", ""):
                    mp.put(infoArtistas, cid1, aw)
        if str(cid1[1:-1]) == str(aw["ConstituentID"][1:-1]):
            mp.put(infoArtistas, cid1, aw)

        i+=1

    print(infoArtistas)
        
def clasificarArtworksArtistaPorTecnica(catalog, nombre):
    i = 1

    obrasArtista = lt.newList("ARRAY_LIST")
    Id_Artista = FindIDArtist(catalog, nombre)
    for i in catalog["constituentid"]["table"]["elements"]:
        if i["key"] == Id_Artista:
            lt.addLast(obrasArtista, i["value"])

    obras = mp.get(catalog["constituentid"], Id_Artista)
    obras = me.getValue(obras)


    cantidad_obras = lt.size(obrasArtista)
    tecnicas = contar_tecnicas(obrasArtista)
    tecnicaMasUsada = tecnica_mas_usada(obrasArtista)
    obras_tecnicaUsada, longitud = obrasTecnicaMasUsada(obrasArtista, tecnicaMasUsada)
    return(cantidad_obras, tecnicas, tecnicaMasUsada, longitud, obras_tecnicaUsada)

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

    tecnicas = lt.newList("ARRAY_LIST")
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
        for obra1 in range(len(obras)):
            if obras[obra]["Medium"] == obras[obra1]["Medium"]:
                iguales += 1   
        dic[obras[obra]["Medium"]] = iguales
    mayor = 0 
    tecnicaMasUsada = ""    
    for llave in dic:
        if dic[llave] > mayor:
           mayor = dic[llave]
           tecnicaMasUsada = llave

    return tecnicaMasUsada

def obrasTecnicaMasUsada(obrasArtista, obramayor):

    obrasA = obrasArtista["elements"]
    obras = lt.newList(datastructure='ARRAY_LIST')

    for i in range(len(obrasA)):
        if obrasA[i]["Medium"] == obramayor:
            lt.addLast(obras, obrasA[i])
    obrasTecnica = obras["elements"]
    longitud = len(obrasTecnica)

    return obrasTecnica, longitud