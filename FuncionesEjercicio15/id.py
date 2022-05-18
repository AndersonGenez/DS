def generarId(nombre, apellido, dni) :
	id = nombre	+ str(len(apellido))
	strDNI = str(dni)
	strDNI = f'{strDNI[0]}{strDNI[1]}{strDNI[2]}'
	id += strDNI

	return id
