'''
3- Desarrollar una función que solicite tres números y calcule el promedio y retorne este valor. 
'''

def prom(cal1, cal2, cal3) :
    return (cal1 + cal2 + cal3) / 3

cal1 = int(input("Ingrese un numero: "))
cal2 = int(input("Ingrese un numero: "))
cal3 = int(input("Ingrese un numero: "))

print(prom(cal1,cal2,cal3))
