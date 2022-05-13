'''
7- Modificar utilizando dos archivos independientes para las funciones y el programa principal
utilizando import 
'''

from modulos import perimetro, superficie

eleccion = int(input('Ingrese 1 para calcular el perimetro del cuadrado: \n ingrese 2 para calcular la superficie: '))

medida = int(input('Ingrese un lado del cuadrado: '))

if eleccion == 1 :
    perimetro(medida)

elif eleccion == 2 :
    superficie(medida)
