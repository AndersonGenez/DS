import os
def init()
print("**** ADMINISTRAR ARCHIVOS ****") opción-input ("Selecciona una opción c=crear y e-eliminar ") if (opcion=="C"):
ruta- input ("Indique la ruta, sino se tomará la actual: ") if (ruta==""): ruta=0s.getcwd()+"\\" #comprobar si la ruta existe if (os.path.isdir (ruta)) :
tipo - input ("Indique el tipo a-archivo y c-carpeta: ") if (tipo=="a"):
archivo-input ("Indique el nombre del Archivo: ") #Crear el archivo manejador-open (ruta+archivo, "W") manejador.close()
print("Archivo", archivo, "creado con exito") elif (tipo="c")
carpeta-input ("Indique el nombre de la carpeta" ) 03.mkdir (ruta+carpeta)
print("Carpeta ", carpeta, "creada con exito") else: init() elif (opcion="e"):
ruta- input ("Indique la ruta, sino se tomará la actual: ") if (ruta==""): ruta-os.getowd()+"\\" eliminar - input ("Indique el nombre de la carpeta o archivo a elimi if (os.path.isfile (ruta+eliminar)):
os.remove (ruta+eliminar)
print("Archivo ", eliminar, "eliminado con éxito") elif (os.path.isdir (ruta+eliminar)):
os. rmdir (ruta+eliminar) else:
init() else: init()

