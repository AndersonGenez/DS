'''
5- Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si
quiere calcular y mostrar su perímetro o su superficie y en función de eso llame a la función
perímetro o superficie.
'''

def perimetro(lado) :
    print(lado * 4)

def superficie(lado) :
    print(lado * lado)


eleccion = int(input('Ingrese 1 para calcular el perimetro del cuadrado: \n ingrese 2 para calcular la superficie: '))

medida = int(input('Ingrese un lado del cuadrado: '))

if eleccion == 1 :
    perimetro(medida)

elif eleccion == 2 :
    superficie(medida)

