def validarDNI (num) :
  res = True
  if len(str(num)) < 7 or len(str(num)) > 8 :
    res = False

  return res

def obtenerDNI() :
    resDNI = ''
    while resDNI == False or resDNI == '' :
        dni = int(input('Ingrese un DNI válido: '))
        resDNI = validarDNI(dni)
    
    return dni