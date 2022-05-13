#6- Modificar el código anterior para que en función retorne el valor calculado.


def perimetro(lado) :
    return (lado * 4)

def superficie(lado) :
    return (lado * lado)


eleccion = int(input('Ingrese 1 para calcular el perimetro del cuadrado: \n ingrese 2 para calcular la superficie: '))

medida = int(input('Ingrese un lado del cuadrado: '))

if eleccion == 1 :
    print(perimetro(medida))

elif eleccion == 2 :
    print(superficie(medida))

