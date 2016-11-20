# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:12:54 2016

@author: alana
"""

class mapa():
    def __init__(self, direcciones="", marcas=""):
        self.direcciones = direcciones
        self.marcas = marcas
        self.url = self.get_direccion(self.direcciones, self.marcas)   
        
    def get_direccion(self , direcciones = "", marcas = ""):
        url = "https://maps.googleapis.com/maps/api/staticmap?"
    
        center ="center=Argentina"
        zoom = "&zoom=4"
        size = "&size=600x640"
        markers = "&markers=" + direcciones
        path = "&path=" + marcas
        imgformat = "&format=png"
        maptype="&maptype=roadmap"
        sensor = "&sensor=false"
        url = url + center + zoom + size + markers+ path + imgformat+maptype + sensor
        print(url)
        return url
        
    def get_url(self):
        self.url = self.get_direccion(self.direcciones , self.marcas)
        return self.url