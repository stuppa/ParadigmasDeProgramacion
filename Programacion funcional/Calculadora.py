
def Obtener_numeros(*args):
    numeros = [*args]
    return numeros

numeros = Obtener_numeros(1,2,3,4,5,6,7)

def suma():
    suma = 0
    for num in numeros:
        suma += num
    return suma
def resta(numero):
    resta = numero
    for num in numeros:
        resta -= num
    return resta
    
def multiplicacion():
    multiplicacion = 1
    for num in numeros:
        multiplicacion = num * multiplicacion
    return multiplicacion   

def division(num1,num2):
    division = num1 / num2
    return division

def modulo(num):
    modulo = num % 2
    return modulo

def main():
    print(''' Caluladora 
    1: suma
    2: resta
    3: multiplicacion
    4: division
    5: modulo''')

    resp = input('Escoge una opcion: ') 

    if resp == '1':
        print("La suma: " + str(suma()))
    elif resp == '2':
        numero = int(input("Ingresa el numero a restar: "))
        restar = resta(numero)
        print("La resta: " + str(restar))
    elif resp == '3':
        print("La multiplicacion: " + str(multiplicacion()))
    elif resp == '4':
        print("La division: " + str(division(numeros[0],numeros[1])))
    elif resp == '5':
        print("El modulo: " + str(modulo(numeros[0])))

