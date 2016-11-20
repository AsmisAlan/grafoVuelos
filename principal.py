# -*- coding: utf-8 -*-

#from ElPadreDeLosGrafos import Grafo, cargar_grafo, barrido, busqueda, mapa

import sys
from PyQt4 import QtGui, uic, QtCore
#import BuscarRuta
from Mapa import mapa
from MenuCrearVuelo import MenuCrear
from NuevosAeropuertos import MenuNuevoAeropuerto 
import TDAgrafo
import htmlGenerator
#from Alta import VentanaAlta


menu = uic.loadUiType("mapa.ui")[0]

class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):        
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        #defino las accciones de los botones
        self.ActualizarMapa.clicked.connect(self.ver_ciudades)
        self.MostrarRuta.clicked.connect(self.ver_ruta)
        self.BuscarVuelo.clicked.connect(self.agregar_ruta)
        self.CrearNuevoVuelo.clicked.connect(self.CrearVuelo)               
        self.AgregarAeropuerto.clicked.connect(self.Agregar_Aeropuerto)
        
        #inicializamos el grafo
        self.grafo = TDAgrafo.inicializar()
        self.grafo.mostrar()
        
        #self.grafo = Grafo()
        #cargar_grafo(self.grafo)
        #barrido(self.grafo)
        self.mapa_ciudades = mapa()
        self.ver_ciudades()
        self.actualizarCiudades()
        
    def ver_ciudades(self):
        lista = self.grafo.ListaVertices()
        self.mapa_ciudades.direcciones = "|".join(lista)
        self.mapa_ciudades.marcas = ""      
        self.visor.load(QtCore.QUrl(self.mapa_ciudades.get_url()))

    def actualizarCiudades(self):
        lista = self.grafo.ListaVertices()
        self.line_origen.setCompleter(QtGui.QCompleter(lista,self.line_origen))
        self.line_destino.setCompleter(QtGui.QCompleter(lista,self.line_destino))
        print("agregue")
        print(lista)

    def ver_ruta(self):
        lista = []
        #aux = busqueda(self.grafo, "Buenos Aires")
        origen = str(self.line_origen.text())
        destino = str(self.line_destino.text())
        lista = TDAgrafo.pt(self.grafo,origen,destino)[0]
        
        self.mapa_ciudades.direcciones = "|".join(lista)
        self.mapa_ciudades.marcas = "|".join(lista)     
        self.visor.load(QtCore.QUrl(self.mapa_ciudades.get_url()))
        """
        lista.append(aux.info)
        aux = aux.arista.cab
        while aux!=None:
            lista.append(aux.info)
            aux = aux.sig
        cadena = "|"
        self.mapa_ciudades.marcas = cadena.join(lista)
        self.visor.load(QtCore.QUrl(self.mapa_ciudades.get_url()))
        """
        
    def agregar_ruta(self):
         ruta = BuscarRuta.MenuBuscar(self.grafo)
         ruta.show()
         ruta.exec_()

    def CrearVuelo (self):
        """ agrega una relacion entre los aeropuertos (aristas) """
        Vuelo = MenuCrear(self,self.grafo )
        Vuelo.show()
        Vuelo.exec_() 
        
        
    def Agregar_Aeropuerto (self):
        """ agrega una ciudad nueva (vertice) """
        Aeropuerto = MenuNuevoAeropuerto(self, self.grafo)
        Aeropuerto.show()
        Aeropuerto.exec_()
        self.actualizarCiudades()
        self.ver_ciudades()
        
        
        
        
app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
sys.exit(app.exec_())