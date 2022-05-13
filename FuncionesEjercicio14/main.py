'''
14- Se necesita desarrolla un programa para facturar. Ingresar Artículo, precio unitario y cantidad
llamar a una función que calcule el importe total de la venta. También desarrollar una función
de determine si se le debe realizar un descuento o no. Si la venta es superior a $15000 debe
realizar un descuento del 8% si es mayor a $30000 15%. Mostrar el total de la venta y el
descuento.
'''

from ecomm import calcCosto, calcDescuento 

carrito = {
    'articulo': '',
    'cantidad': 0,
    'precio-unitario': 0,
    'subtotal': 0,
    'precio-final': 0
    }

carrito['articulo'] = input('Ingrese el nombre del articulo: ')
carrito['precio-unitario'] = int(input('Ingrese el precio del articulo: '))
carrito['cantidad'] = int(input('Ingrese cantidad del articulo: '))

carrito['subtotal'] = calcCosto(carrito['precio-unitario'], carrito['cantidad'])

carrito['precio-final'] = calcDescuento(carrito['subtotal'])

print(f"Total: {carrito['precio-final']} Descuento: {round(carrito['subtotal'] - carrito['precio-final'], 2)}")