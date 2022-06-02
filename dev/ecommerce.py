def calcular_precio_envio(subtotal, producto, cantidad, cp) :
    precioEnvio = 850
    productosConRegla = ('camiseta', 'short')

    #Envio gratis para Rosario
    if cp == 2000 or cp == 2001 :
        precioEnvio = 0

    #Envio gratis para compras desde $6000
    elif subtotal > 5999 :
        precioEnvio = 0

    #40% off para compras mayores a 3 productos
    elif producto in productosConRegla :
        if cantidad > 3 :
            precioEnvio = precioEnvio * 0.6

    return precioEnvio

def calcular_subtotal(precioUnidad, cantidad) :
    return precioUnidad * cantidad