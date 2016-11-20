# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:17:09 2015

@author: alan
"""

import shelve


class Vertice():
    ciudad = None # datos complementarios del vertice.
    estado = None
    
class Arista():
    origen ,destino= None,None #Guardo las relaciones entre los vertices.
    ha,hs,fecha = None,None,None # guardo los datos coplementarios.
    precio = None # guardo el precio del vuelo.
    distancia = None # guarda la distancia entre los vuelos.
    estado = None 

def abrir(ruta):
	return shelve.open(ruta)

def cerrar(archivo):
	archivo.close()

def leer(archivo,pos):
	try:
		return archivo[str(pos)]
	except:
		return None
	
def guardar(archivo, dato):
	try:
		archivo[str(len(archivo))] = dato
		return True
	except:
		raise None

def modificar(archivo, dato, pos):
	try:
		archivo[str(pos)] = dato
		return True
	except:
		raise None
  
  