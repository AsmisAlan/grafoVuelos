# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:38:43 2015

@author: alan
"""

import archivo
import Constantes
from PyQt4 import QtGui , Qt , QtCore

def add_in_tabla(tabla,aux,dato):
    tabla.insertRow(aux)
    nombre = QtGui.QTableWidgetItem(dato.tit)
    tel = QtGui.QTableWidgetItem( str(dato.tel))
    direc = QtGui.QTableWidgetItem(dato.direc)
    tabla.setItem(aux ,0, nombre )
    tabla.setItem(aux ,1,tel )
    tabla.setItem(aux ,2,direc )
    
def CargarTablaRelaciones(lista,tabla):
        fila = 0
        if tabla.rowCount() < len(lista):
            tabla.setRowCount(len(lista) )
        #limpiar(tabla)
        for aux in lista:
            clave = QtGui.QTableWidgetItem(str(aux[1]))
            nombre = QtGui.QTableWidgetItem(aux[0].nombre)
            rel = QtGui.QTableWidgetItem(aux[0].relacion)
            dur = QtGui.QTableWidgetItem(str(aux[0].duracion))
            #tooltips
            clave.setToolTip(aux[0].descripcion)
            nombre.setToolTip(aux[0].descripcion)
            rel.setToolTip(aux[0].descripcion)
            dur.setToolTip(aux[0].descripcion)
            #color si esta dado de baja
            if not aux[0].estado :
                #color texto
                clave.setTextColor(QtGui.QColor(255,255,255))
                nombre.setTextColor(QtGui.QColor(255,255,255))
                rel.setTextColor(QtGui.QColor(255,255,255))
                dur.setTextColor(QtGui.QColor(255,255,255))
                #color de fondiu    
                clave.setBackground(QtGui.QColor(179,36,40))
                nombre.setBackground(QtGui.QColor(179,36,40))
                rel.setBackground(QtGui.QColor(179,36,40))
                dur.setBackground(QtGui.QColor(179,36,40))
            tabla.setItem(fila,0, clave)
            tabla.setItem(fila,1, rel)
            tabla.setItem(fila,3, nombre)
            tabla.setItem(fila,2, dur)
            fila+=1


    
def CargarTabla(grafo,tabla):
        fila = 0
        tabla.setRowCount(grafo.tamanioGrafo())
        arch= archivo.abrir(Constantes.DirVertices) #abro archivo vertices
        limpiar(tabla)
        lista = grafo.ListaVertices()
        for aux in lista:
            dato = archivo.leer(arch,lista[fila])
            nombre = QtGui.QTableWidgetItem(str(aux)+': '+dato.nombre)
            nombre.setToolTip('Descripcion:<b>'+dato.descripcion+'</b>.')
            tabla.setVerticalHeaderItem(fila , nombre )
            
            dibujarRelaciones (fila ,tabla,grafo,lista[fila])      
            
            fila+=1
        archivo.cerrar(arch)
        
        
def dibujarRelaciones (fila ,tabla,grafo,nodo):
    listaArista = grafo.listaAristas(nodo)
    if tabla.columnCount() <= len(listaArista) * 2:
        tabla.setColumnCount(len(listaArista) * 2)
    cont = 0
    arch = archivo.abrir(Constantes.DirAristas)
    for arista in listaArista:
        relaciones = archivo.leer(arch , arista[1]) #leo la pos de la arista
        t = QtGui.QTableWidgetItem(relaciones.nombre.upper())
        t.setBackground(QtGui.QColor(59,131,189))
        t.setToolTip('Descripcion:<b>'+relaciones.descripcion+'</b>. Duracion: '+str(relaciones.duracion))
        tabla.setItem(fila,cont,t)
        tabla.setHorizontalHeaderItem(cont, QtGui.QTableWidgetItem('TAREA'))
        
        cont +=1        
        t = QtGui.QTableWidgetItem( 'VERTICE: '+ str(arista[0]) )
        tabla.setItem(fila,cont,t)
        tabla.setHorizontalHeaderItem(cont, QtGui.QTableWidgetItem('VERTICE'))        
        
        cont +=1 
    archivo.cerrar(arch)
        
        
    
        
def ActulizarTabla(grafo,tabla):
        fila = 0
        if tabla.rowCount() < grafo.tamanioGrafo():
            tabla.insertRow(grafo.tamanioGrafo() - 1)
        limpiar(tabla)
        lista = grafo.ListaVertices()
        arch= archivo.abrir(Constantes.DirVertices) #abro el arch de vertices
        for aux in lista:
            dato = archivo.leer(arch,lista[fila])
            nombre = QtGui.QTableWidgetItem(str(dato.nombre))
            tabla.setVerticalHeaderItem(fila , nombre )
            fila+=1
        archivo.cerrar(arch)
            
            
def setChangeTabla(tabla,lista,aux,pos):
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    apellido =QtGui.QTableWidgetItem( lista.obtener(aux).get_apellido() )
    dni = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_DNI()) )
    tel = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_telefono() ))
    direc = QtGui.QTableWidgetItem( lista.obtener(aux).get_direc() )
    tabla.setItem(pos ,0 , dni)
    tabla.setItem(pos ,1 , nombre )
    tabla.setItem(pos ,2, apellido)
    tabla.setItem(pos ,3 ,tel )
    tabla.setItem(pos ,4,direc )
    
def limpiar(tabla, tam = 100):
    tabla.clear()
    


