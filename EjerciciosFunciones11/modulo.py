
def obtenerLenUltimaPalabra (texto) :
    palabras = texto.split(' ')

    palabraFinal = palabras[-1]

    while palabraFinal == '' :
        palabras.pop()
        palabraFinal = palabras[-1]

    return len(palabraFinal)
