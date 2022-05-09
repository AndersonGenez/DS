'''
8- El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1
pero en su lugar imprime 5. ¿Qué hay que corregir?
'''
# def calcular (x, y) :
#   print(((x + y) * x) / (x + y))

# calcular(5, 1)


# def calcular (x, y) :
#   print(((x + y) * x) / (x * x))

# calcular(5, 1)

# 9- Escribir una función que, dado un número de DNI, retorne True si el número es válido y False
# si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígito

def validarDNI (num) :
  res = True
  if len(str(num)) < 7 or len(str(num)) > 8 :
    res = False

  return res

print(validarDNI(0))
