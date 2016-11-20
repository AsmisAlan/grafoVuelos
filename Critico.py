# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:46:07 2015

@author: alan
"""
from PyQt4 import QtGui, uic
import pertCPM
import TDAgrafo

puntoCritico = uic.loadUiType("Critico.ui")[0]
class PuntoCritico(QtGui.QWidget,puntoCritico ):
    
    def __init__(self,grafo,parent=None):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         self.grafo = grafo
         lista = self.grafo.listaNombresVertices()
         self.verticeBox.addItems(lista)
         lista.remove(lista[0])
         self.relacionBox.addItems(lista)
         self.ver.clicked.connect(self.mostrar)
    
    def mostrar(self):
        vertice = self.verticeBox.currentText() #"""ACA HAY QUE MODIFICAR"""
        vertice = vertice[0:vertice.index(':')]

        relacion= self.relacionBox.currentText() #"""ACA HAY QUE MODIFICAR"""
        relacion= relacion[0:relacion.index(':')]
        self.pertCPM = pertCPM.PERT(self.grafo,TDAgrafo.pt(self.grafo,vertice,relacion))