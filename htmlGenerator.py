# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 03:20:41 2016

@author: alana
"""

class googleMap():
    
    def __init__(self):
        #texto , latitud , longitud, marker
        self.dir = []
        
    def addDir(self, info):
        self.dir.append(info)
    
    def clear(self):
        self.dir = []
        
    def getHtml(self):
        html = """
                <html>
                <head>
                  <title>Google Maps Multiple Markers</title>
                  <script src="http://maps.google.com/maps/api/js?sensor=false" type="text/javascript"></script>
                </head>
                <body>
                  <div id="map" style="height: 100%; width: 100%;">
                </div>
                <script type="text/javascript">
                    var locations = """+str(self.dir)+""";
                    
                    var map = new google.maps.Map(document.getElementById('map'), {
                      zoom: 10,
                      center: new google.maps.LatLng(locations[0][1], locations[0][2]),
                      mapTypeId: google.maps.MapTypeId.ROADMAP
                    });
                
                    var infowindow = new google.maps.InfoWindow();
                
                    var marker, i;
                    
                    var bounds = new google.maps.LatLngBounds();
                
                    for (i = 0; i < locations.length; i++) { 
                      marker = new google.maps.Marker({
                        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                        icon: locations[i][3],
                        map: map
                      });
                      bounds.extend(marker.getPosition());
                      google.maps.event.addListener(marker, 'click', (function(marker, i) {
                        return function() {
                          infowindow.setContent(locations[i][0]);
                          infowindow.open(map, marker);
                        }
                      })(marker, i));
                    }
                    map.fitBounds(bounds);
                  </script>
                </body>
                </html>
                            """
        return html
        

if(__name__ == "__main__"):
    a = googleMap()
    a.addDir(["pikachu",-23.12312123,-56.123123123,"http://icons.iconarchive.com/icons/hektakun/pokemon/72/025-Pikachu-icon.png"])
    a.addDir(["bolbasor",-23.52312123,-56.623123123,"http://icons.iconarchive.com/icons/hektakun/pokemon/72/025-Pikachu-icon.png"])
    a.addDir(["raichu",-23.32312123,-56.123123123,"http://icons.iconarchive.com/icons/hektakun/pokemon/72/025-Pikachu-icon.png"])
    a.addDir(["mantis",-23.52312123,-56.623123123,"http://icons.iconarchive.com/icons/hektakun/pokemon/72/025-Pikachu-icon.png"])
    print(a.getHtml())