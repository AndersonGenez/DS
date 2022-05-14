def crearCarpeta() :
    carpeta=input ("Indique el nombre de la carpeta" )
    os.mkdir (ruta+carpeta)
    print("Carpeta ", carpeta, "creada con exito")