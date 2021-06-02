from Calculadora import Calculadora

print(''' Caluladora 
1: suma
2: resta
3: multiplicacion
4: division
5: modulo''')

resp = input('Escoge una opcion: ')

lista_numeros = []
rp = "s"
while rp == "s":
    num = int(input("Numero: "))
    lista_numeros.append(num)
    rp = input("Agregar otro numero?s/n: ")

cal = Calculadora(lista_numeros)

if resp == '1':
    print("La suma: " + str(cal.suma()))
elif resp == '2':
    numero = int(input("Ingresa el numero a restar: "))
    resta = cal.resta(numero)
    print("La resta: " + str(resta))
elif resp == '3':
    print("La multiplicacion: " + str(cal.multiplicacion()))
elif resp == '4':
    print("La division: " + str(cal.division(lista_numeros[0],lista_numeros[1])))
elif resp == '5':
    print("El modulo: " + str(cal.modulo(lista_numeros[0])))