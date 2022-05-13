'''
15- Escribir un programa que permita al usuario obtener un identificador para cada uno de los
socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio,
indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse
más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más
de un apellido, el usuario sólo ingresará uno.
'''

socios = []

nombreSocio = input('Ingrese su primer nombre: ')

while nombreSocio != '' :
    nuevoSocio = {}
    nuevoSocio['nombre1'] = nombreSocio
    nuevoSocio['nombre2'] = input('Ingrese su segundo nombre: \n Presione Enter en caso de no tener segundo nombre. ')
    nuevoSocio['apellido'] = input('Ingrese su primer apellido: ')
    nuevoSocio['dni'] = int(input('Ingrese su DNI: '))
    socios.append(nuevoSocio)

    nombreSocio = input('Ingrese su primer nombre: ')

print(socios)