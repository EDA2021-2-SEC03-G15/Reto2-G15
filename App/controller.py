import config as cf
import model
import csv

def initCatalog():

    catalog = model.newCatalog()
    return catalog

def loadArtists(catalog):

    model.loadArtists(catalog)

def loadArtworks(catalog):

    model.loadArtworks(catalog)

def ordenarArtistasReq1(catalog, inicio, fin):

    return model.ordenarArtistasReq1(catalog, inicio, fin)

def ordenarArtworksReq2(catalog, inicio, fin):

    return model.ordenarArtworksReq2(catalog, inicio, fin)

def clasificarObrasNacionalidadReq4(catalog):

    return model.clasificarObrasNacionalidadReq4(catalog)