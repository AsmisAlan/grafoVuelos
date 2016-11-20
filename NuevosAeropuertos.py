# -*- coding: utf-8 -*-
from PyQt4 import QtGui, uic, QtCore
import archivo 
import Constantes
#import ElPadreDeLosGrafos

menu = uic.loadUiType("NuevoAeropuerto.ui")[0]

class MenuNuevoAeropuerto(QtGui.QDialog, menu):

    def __init__(self, padre = None, grafo = None , pos = None ):        
        QtGui.QDialog.__init__(self,padre)
        self.setupUi(self)
        self.grafo = grafo
        self.guardar_nueva.clicked.connect(self.guardarNuevoAeropuerto)
        
    def guardarNuevoAeropuerto(self):
        if (self.grafo.ConsultarVertice(str(self.line_nueva.text())) != None):
            print("ya existelacudad")
        else:
            city = archivo.Vertice()
            city.ciudad = str(self.line_nueva.text())
            city.estado = True
            arch= archivo.abrir(Constantes.DirVertices)
            pos =len(arch)
            archivo.guardar(arch , city)
            archivo.cerrar(arch)
            self.grafo.insertarVertice(city.ciudad , pos)
            self.grafo.mostrar()
            self.close()