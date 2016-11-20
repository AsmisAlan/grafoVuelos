# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:16:52 2015

@author: alan
"""
from TDAvertice import Arista , NodoArista
import archivo
import Constantes
import TDAPILA

class NodoVertice ():
    siguiente_vertice, clave, pos, aristas = None, None ,None , None
    def __Init__(self):
        pass
    
class Grafo():
    def __init__(self):
        self.cab = None
        self.tamanio = 0
        
    def insertarVertice (self, ciudad , pos):
        """iserta un vertice en el grafo"""
        dir = NodoVertice()
        dir.clave =ciudad
        dir.pos = pos
        dir.siguiente_vertice = None
        dir.aristas= Arista()
        self.tamanio+=1
        if (self.cab == None) or (ciudad < self.cab.clave):
            dir.siguiente_vertice=self.cab
            self.cab = dir
        else:
            anterior = self.cab
            actual = self.cab.siguiente_vertice
            while (actual != None) and (actual.clave < ciudad):
                anterior = anterior.siguiente_vertice
                actual = actual.siguiente_vertice
            dir.siguiente_vertice = actual
            anterior.siguiente_vertice = dir
            
    def insertarRelacion(self, vertice , relacion):
        pos = self.ConsultarVertice(vertice) 
        if(pos != None): # existe el vetice de origen???
            if(self.ConsultarVertice(relacion.clave) != None): #existe el vertice de destino???
                if(pos.aristas.ConsultarAristas(relacion.clave) == None): #existe ya una relacion????
                    pos.aristas.insertarArista(relacion) # agraga la clave y la pos del arch de aristas
                    return ''
                else:
                    return 'ya existe la relacion entre' + vertice + " y " + destino.clave
            else:
                return'ERROR no existe el vertice destino' + relacion.clave
        else:
            return 'ERROR no existe el vertice origen' + vertice
        
        
    """
    def insertarRelacion(self, vertice , relacion):
        posVertice = self.ConsultarVertice(vertice) 
        if(posVertice != None):
            posArista = self.ConsultarVertice(relacion) 
            if(posArista != None):
                if(posVertice.aristas.ConsultarAristas(relacion) == None):
                    if(posArista.aristas.ConsultarAristas(vertice) == None ):
                        posVertice.aristas.insertarArista(relacion)
                    else:
                        return 'ya existe la relacion.'
                else:
                    return 'ya existe la relacion.'
            else:
                return'ERROR no existe el vertice ' + relacion
        else:
            return 'ERROR no existe el vertice ' + vertice
    """
            
    def eliminarVertice(self,kx):
        """Elimina un vertice, devuelve el valor"""
        if (kx == self.cab.clave):
            x = self.cab.clave
            dir = self.cab
            self.cab = dir.siguiente_vertice
            self.tamanio -= 1
        else:
            ante = self.cab
            act = self.cab.siguiente_vertice
            while (act != None) and (kx != act.clave):
                ante=ante.siguiente_vertice
                act = act.siguiente_vertice
            if (act != None):
                x = act.clave
                ante.siguiente_vertice = act.siguiente_vertice
                self.tamanio -= 1
            else:
                x = 0; 
        if (x != 0):
            Nw = self.cab
            while Nw != None:
                Nw.aristas.eliminarArista(kx)
                Nw = Nw.siguiente_vertice
        return x 
    
    def eliminarArista(self,clave,arista):
        self.ConsultarVertice(clave).aristas.eliminarArista(arista)
        
    def ConsultarVertice (self,kx):
        pos = self.cab
        while (pos != None) and (kx != pos.clave):
            pos= pos.siguiente_vertice
        return pos
    
    def existeVertice (self,origen):
        """ devuelve verdadero si existe el vertice """
        pos = self.cab
        while (pos != None) and (origen != pos.clave):
            pos= pos.siguiente_vertice
        return True if pos != None else False
        
    def existeArista(self, origen , destino):
        """ asumiendo que el origen existe, busco si existe el destino """
        pos = self.ConsultarVertice(origen).aristas.ConsultarAristas(destino)
        return True if pos != None else False

        
    def mostrar (self):
        Nw = self.cab
        while Nw != None:
            print(Nw.clave)
            Nw.aristas.mostrar()
            Nw = Nw.siguiente_vertice
        
            
    def listaAristas(self,clave):
        return self.ConsultarVertice(clave).aristas.ListaAristas()
    
    def listaAristasModificar(self,clave):
        return self.ConsultarVertice(clave).aristas.ListaAristasModificable()
    
    def listaAristasDur(self,clave):
        return self.ConsultarVertice(clave).aristas.listaAristasDur()
        
    def tamanioAristas(self,clave):
        return self.ConsultarVertice(clave).aristas.tamanioArista()
          
    def ListaVertices(self):
        """ devuelve una lista con todos los vertices que contiene el grafo """
        lista = []
        Nw = self.cab
        while Nw != None:
            lista.append(Nw.clave)
            Nw = Nw.siguiente_vertice
        return lista
    
    def listaNombresVertices(self):
        lista = []
        Nw = self.cab
        vert = archivo.abrir(Constantes.DirVertices)
        while Nw != None:
            lista.append(str(Nw.clave)+': '+archivo.leer(vert,Nw.clave).nombre)
            Nw = Nw.siguiente_vertice
        archivo.cerrar(vert)
        return lista
    
    def tamanioGrafo(self):
        return self.tamanio
        
    def GrafoLleno (self):
        return (self.cab > 100)
        
    def GrafoVaci0 (self):
        return (self.cab == None)
        
    def modificarPesoArista(self,clave,arista,duracion):
        self.ConsultarVertice(clave).aristas.modificarArista(arista , duracion)
        
        
def inicializar():
    """ esta funcion crea y carga un grafo, luego me lo retorna"""
    a = Grafo()
    Arch = archivo.abrir(Constantes.DirVertices) #abro el arch de vertices
    cont = 0
    while (cont < len(Arch)):
        dato = archivo.leer(Arch,cont)
        if dato.estado : 
            #vertAux = NodoVertice()
            #vertAux.clave = dato.ciudad #nombre de la ciudad
            #vertAux.pos = cont # posicion en el archivo
            a.insertarVertice(dato.ciudad , cont)
        cont +=1
    archivo.cerrar(Arch)
    
    Arch2 = archivo.abrir(Constantes.DirAristas) # abro el arch de aristas
    cont = 0 # renuevo la variable de control
    while (cont < len(Arch2)):
        dato = archivo.leer(Arch2,cont)
        if dato.estado : 
            relacion = NodoArista()
            relacion.clave = dato.destino #nombre de la ciudad de destino
            relacion.pos = cont
            relacion.peso = dato.distancia # duracion de la arista
            a.insertarRelacion(dato.origen, relacion)
        cont +=1
    archivo.cerrar(Arch2)
    return a
    
        
        
def pt(grafo, ini , fin):
    #camino = []
    pila = TDAPILA.Pila()
    hayPaso(grafo,pila,[],ini,fin)
    if pila.tam > 0 :
        return menor(pila)
    else:
        return [[],0]
        
def hayPaso(grafo , pila , camino , inicio , fin , dur = 0):
    import copy    
    listaAirstas = grafo.listaAristasDur(inicio)
    if len(listaAirstas) > 0 : #me fijo si las aristas no estan vacias
        camino.append(inicio)
        durAux = int(existe(fin,listaAirstas))
        if (durAux > -1):#me fijo si fin esta dentro de las aristas
            dur += durAux
            camino.append(fin)
            pila.apilar([copy.copy(camino),dur])
            dur -= durAux
        for arista in listaAirstas:
            hayPaso(grafo,pila,camino,arista[0],fin,dur + int(arista[1]))
            if len(camino) >  0:
                camino.pop()
                
                
                
def hayPaso2(grafo , pila , camino , inicio , fin , dur = 0):
    import copy    
    listaAirstas = grafo.listaAristasDur(inicio)
    if len(listaAirstas) > 0 : #me fijo si las aristas no estan vacias
        camino.append(inicio)
        durAux = int(existe(fin,listaAirstas))
        if (durAux > -1):#me fijo si fin esta dentro de las aristas
            dur += durAux
            camino.append(fin)
            print(camino)
            pila.apilar([copy.copy(camino),dur])
            dur = 0
            #camino = ['0']
        for arista in listaAirstas:
            if (fin in camino):
                hayPaso(grafo,pila,[copy.copy(camino[0])],arista[0],fin,dur + arista[1])
            else:
                hayPaso(grafo,pila,camino,arista[0],fin,dur + arista[1])
                
def existe(fin , listaA):
    tiempo = -1
    for arista in listaA:
        if arista[0] == fin :
            tiempo =  arista[1]
            break
    return tiempo
    
def mayor(pila):
    critico = 0
    while pila.tam > 0 :
        lista = pila.desapilar()
        print(lista[0])
        print(lista[1])
        if lista[1] > critico:
            critico = lista[1]
            camino = lista
    return camino
        
def menor(pila):
    lista = pila.desapilar()
    pila.apilar(lista)
    critico = lista[1]
    while pila.tam > 0 :
        lista = pila.desapilar()
        print(lista[0])
        print(lista[1])
        if lista[1] < critico:
            critico = lista[1]
            camino = lista
    return camino























    
    