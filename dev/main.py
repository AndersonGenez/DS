from ecommerce import calcular_precio_envio, calcular_subtotal

productos = {
'a': { 'nombre': 'camiseta', 'precio': 1000 },
'b': { 'nombre': 'campera', 'precio': 2500 },
'c': { 'nombre': 'short', 'precio': 900 },
'd': { 'nombre': 'pantalon', 'precio': 1800 },
'e': { 'nombre': 'bolso', 'precio': 1400 }
}

print('-----------------------------------')
print('Seleccione un producto para comprar')
print('-----------------------------------')
print('A) Camiseta\nB) Short\nC) Campera\nD) Pantalon\nE) Bolso')

eleccion = input(':')
producto = productos[eleccion]
cantidad = int(input('Ingrese la cantidad que sea: '))
cp = int(input('Ingrese su codigo postal'))
subtotal = calcular_subtotal(producto.precio, cantidad)
#print(calc.calcular_precio_envio(1200, 'campera', 1, 2000))
#print(calc.calcular_precio_envio(6500, 'campera', 1, 3000))
print(calcular_precio_envio(500, 'short', 2, 3000))
print(producto)
print(subtotal)

