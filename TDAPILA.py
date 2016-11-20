# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:50:16 2015

@author: alan
"""

class nodoPila():
    info,sig=None,None
    
    def __init__(self):
        pass

class Pila():
    def __init__ (self):
        self.tope= None
        self.tam=0
    
    def apilar(self,x):
        dir=nodoPila()
        dir.info=x
        dir.sig=self.tope
        self.tam+=1
        self.tope = dir
        
    def desapilar(self):
        x=self.tope.info
        self.tope=self.tope.sig 
        self.tam-=1
        return x
    
    def pilaVacia(self):
        return self.tope == None
    
    def tamanio(self):
        return self.tam
            
        


        

