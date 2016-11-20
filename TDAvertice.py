# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:06:39 2015

@author: alan
"""
import archivo
import Constantes

class NodoArista ():
    siguiente_arista,clave,pos ,peso = None, None ,None , None
    def __Init__(self):
        pass
    
class Arista():
    def __init__(self):
        self.cab = None
        self.tamanio = 0
        
    def insertarArista (self, x):
        """iserta un vertice en el grafo"""
        dir = NodoArista()
        dir.clave =x.clave
        dir.pos = x.pos
        dir.peso = x.peso
        dir.siguiente_arista = None
        self.tamanio+=1
        if (self.cab == None) or (x.clave < self.cab.clave):
            dir.siguiente_arista=self.cab
            self.cab = dir
        else:
            anterior = self.cab
            actual = self.cab.siguiente_arista
            while (actual != None) and (actual.clave < x.clave):
                anterior = anterior.siguiente_arista
                actual = actual.siguiente_arista
            dir.siguiente_arista = actual
            anterior.siguiente_arista = dir
            
            
    def ConsultarAristas (self,kx):
        pos = self.cab
        while (pos != None) and (kx != pos.clave):
            pos= pos.siguiente_arista
        return pos
            
    def modificarArista(self,arista , newDur):
        self.ConsultarAristas(arista).peso = newDur
            
    def eliminarArista(self,kx):
        if self.cab!= None :
            if (kx == self.cab.clave):
                x = self.cab.clave
                dir = self.cab
                self.cab = dir.siguiente_arista
                self.tamanio -= 1
            else:
                ante = self.cab
                act = self.cab.siguiente_arista
                while (act != None) and (kx != act.clave):
                    ante=ante.siguiente_arista
                    act = act.siguiente_arista
                    
                if (act != None):
                    x = act.clave
                    ante.siguiente_arista = act.siguiente_arista
                    self.tamanio -= 1
                else:
                    x = 0;
            return x 
        
        
    def ListaAristas(self):
        Nw = self.cab
        lista =  []
        while Nw != None:
            lista.append([str(Nw.clave) , str(Nw.pos)]) 
            Nw = Nw.siguiente_arista
        return lista
    
    def mostrar(self):
        Nw = self.cab
        while Nw != None:
            print([str(Nw.clave) , str(Nw.pos)]) 
            Nw = Nw.siguiente_arista
        
    def listaAristasDur(self):
        Nw = self.cab
        lista =  []
        while Nw != None:
            lista.append([str(Nw.clave) , Nw.peso]) 
            Nw = Nw.siguiente_arista
        return lista
        
        
        
    def ListaAristasModificable(self):
        Nw = self.cab
        lista =  []
        arista = archivo.abrir(Constantes.DirAristas)
        while Nw != None:
            lista.append([archivo.leer(arista,Nw.pos),Nw.pos]) 
            Nw = Nw.siguiente_arista
        archivo.cerrar(arista)
        return lista
        
    def tamanioArista(self):
        return self.tamanio
            
    
    def VerticeLleno (self):
        return (self.tamanio > 100)
        
        
    def VerticeVacio (self):
        return (self.cab == None)