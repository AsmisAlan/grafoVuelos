import shelve


def crear(ruta):
	return shelve.open(ruta)

def cerrar(archivo):
	archivo.close()

def leer(archivo,pos):
	try:
		return archivo[str(pos)]
	except:
		return None
	
def guardar(archivo, dato):
	try:
		archivo[str(len(archivo))] = dato
		return True
	except:
		raise None

def modificar(archivo, dato, pos):
	try:
		archivo[str(pos)] = dato
		return True
	except:
		raise None
  
  
'''import archivo as A
arch = A.crear ('datos')
S = 'Juan'
A.guardar (arch,S)
S = 'Pedro'
A.guardar (arch, S)
pos = 0
while pos < len (arch)
    dato = A.leer
    print (dato)
    pos += 1
A = open ('articulos.txt')
linea = A.readline()
while (linea)
    trato linea
    linea =A.readline()
A.close ()'''
