class Calculadora:

    def __init__(self,numeros):
        self.numeros = numeros
    
    def suma(self):
        suma = 0
        for num in self.numeros:
            suma += num
        return suma

    def resta(self,numero):
        resta = numero
        for num in self.numeros:
            resta -= num
        return resta
    
    def multiplicacion(self):
        multiplicacion = 1
        for num in self.numeros:
            multiplicacion = num * multiplicacion
        return multiplicacion   
    
    def division(self,num1,num2):
        division = num1 / num2
        return division
    
    def modulo(self,num):
        modulo = num % 2
        return modulo



