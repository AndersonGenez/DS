# 10- Se necesita desarrollar Programa(función)que presupueste cuánto saldrá el alambrado de un
# campo. Para ello ingresar las medidas del terrero y el precio del metro de alambre. Crear un
# módulo para calcular la cantidad de metros necesarios y calcular el costo del alambrado y
# mostrar el costo.

from cantidadMetros import cantidadMetros 
from precioTotal import precioTotal


# medidas = []
precio = float(input('ingrese precio de alambre por metro: '))
alto = int(input('Ingrese el largo del terreno: '))
ancho = int(input('Ingrese el ancho del terreno: '))
perimetro = cantidadMetros(alto, ancho)
total = precioTotal(precio, perimetro)

print('El costo total del alambrado es: ', total)
