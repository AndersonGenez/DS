'''
15- Escribir un programa que permita al usuario obtener un identificador para cada uno de los
socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio,
indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse
más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más
de un apellido, el usuario sólo ingresará uno.

Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa
debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer
nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258
'''

from dni import obtenerDNI
from id import generarId

socios = []

nombreSocio = input('Ingrese su primer nombre: ')

while nombreSocio != '' :
    nuevoSocio = {}
    nuevoSocio['nombre1'] = nombreSocio
    nuevoSocio['nombre2'] = input('Ingrese su segundo nombre: \n Presione Enter en caso de no tener segundo nombre. ')
    nuevoSocio['apellido'] = input('Ingrese su primer apellido: ')
    nuevoSocio['dni'] = obtenerDNI()
    nuevoSocio['id'] = generarId(nuevoSocio['nombre1'], nuevoSocio['apellido'], nuevoSocio['dni'])
    socios.append(nuevoSocio)

    nombreSocio = input('Ingrese su primer nombre: ')

for socio in socios :
    print(f"Socio: {socio['nombre1']} {socio['nombre2']} {socio['apellido']} identificador: {socio['id']}")