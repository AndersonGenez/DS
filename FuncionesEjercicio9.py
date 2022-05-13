# 9- Escribir una función que, dado un número de DNI, retorne True si el número es válido y False
# si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígito

entrada = int(input('Ingrese un DNI'))
def validarDNI (num) :
  res = True
  if len(str(num)) < 7 or len(str(num)) > 8 :
    res = False

  return res

print(validarDNI(entrada))
