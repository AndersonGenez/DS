def maximo(a,b):
    if a>b:
        return a
    else:
        return b
def minimo(a,b):
    if a<b:
        return a
    else:
        return b
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

#Las variables que se ubican dentro de las funciones deben coincidir con los parametros que recibe la misma
