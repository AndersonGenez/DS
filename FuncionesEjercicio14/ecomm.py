def calcCosto (precio, cantidad) :
    return precio * cantidad

def calcDescuento (precio) :
    res = precio

    if precio > 30000 :
        res = precio * 0.85

    elif precio > 15000 :
        res = precio * 0.92

    return res
