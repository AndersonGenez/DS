'''
2- Modificar el código anterior para que la función retorne la suma y se muestre en el programa
que llamó a la función
'''

def suma (cal1,cal2,cal3):
    return cal1 + cal2 + cal3

cal1 = int(input("Ingrese la calificacion a sumar: "))
cal2 = int(input("Ingrese la calificacion a sumar: "))
cal3 = int(input("Ingrese la calificacion a sumar: "))

print(suma(cal1,cal2,cal3))
