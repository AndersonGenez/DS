def capital(palabra) :
    res = ''
    capitalizado = False
    validos = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
    for i in palabra :
        letra = i.lower()
        if letra in validos and capitalizado == False :
            capitalizado = True
            res += i.upper()
        else :
            res += i

    return res

def titulo(texto) :
    res = ''
    liTexto = texto.split(' ')
    for i in liTexto :
        res += capital(i) + ' '
    res.strip(' ')

    return res