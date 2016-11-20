# -*- coding: utf-8 -*-
from PyQt4 import QtGui, uic, QtCore, QtWebKit
#from ElPadreDeLosGrafos import busqueda
import archivo
import Constantes
import TDAvertice
#import ElPadreDeLosGrafos

menu = uic.loadUiType("VentanaVuelo.ui")[0]

class MenuCrear(QtGui.QDialog, menu):
    
    def __init__(self, padre = None, grafo = None , pos = None ):        
        QtGui.QDialog.__init__(self,padre)
        self.setupUi(self)
        self.grafo = grafo
        self.guardar.clicked.connect(self.guardarRegistro)
        self.cargarCiudades()
        if pos != None: 
            print("el pibe quiere modificar")
            self.guardar.close()
        else:
            self.modificar.close()
            print("el loco quiere alta")
            
    def cargarCiudades(self):
        """ carga las ciudades que esta en el grafo, dentro de los lineEdit
        de origen y destinos"""
        lista = self.grafo.ListaVertices()
        self.line_origen.setCompleter(QtGui.QCompleter(lista,self.line_origen))
        self.line_destino.setCompleter(QtGui.QCompleter(lista,self.line_destino))
        
    def guardarRegistro(self):
        if self.grafo.existeVertice(str(self.line_origen.text())):
                if self.grafo.existeVertice(str(self.line_destino.text()) ):
                    if not self.grafo.existeArista(str(self.line_origen.text()) , str(self.line_destino.text()) ): 
                        #crea un registro de tipo arista
                        vuelo = archivo.Arista()
                        vuelo.origen = str(self.line_origen.text())
                        vuelo.destino = str(self.line_destino.text())
                        vuelo.distancia =str(self.line_distancia.text())
                        vuelo.precio = str(self.line_precio.text())
                        vuelo.fecha  = str(self.line_calendario.selectedDate().toString('d/MM/yyyy'))
                        vuelo.hs = str(self.line_salida.text())
                        vuelo.ha = str(self.line_llegada.text() )
                        vuelo.estado = True
                        #guarda en el archivo de aristas el registro
                        arch = archivo.abrir(Constantes.DirAristas)
                        archivo.guardar(arch , vuelo)
                        pos = len(arch)
                        archivo.cerrar(arch)
                        #actualiza el grafo
                        arista = TDAvertice.NodoArista()
                        arista.clave = vuelo.destino
                        arista.peso = vuelo.distancia
                        arista.pos = pos
                        self.grafo.insertarRelacion(vuelo.origen , arista)
                        self.close() #cierra el dialogo
