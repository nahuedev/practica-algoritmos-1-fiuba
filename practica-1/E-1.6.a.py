""" 
Ejercicio 1.6. Escribir funciones que resuelvan los siguientes problemas:
a) Dados dos numeros, imprimir la suma, resta, division y multiplicacion de ambos.
b) Dado un numero entero n, imprimir su tabla de multiplicar.
 """

 # a):

def calcula_suma(a,b):
     return a + b
def calcula_resta(a,b):
     return a - b    

def calcula_divicion(a,b):
     return a / b

def calcula_multiplicacion(a,b):
     return a * b


def calcula_operaciones_basicas(a,b):
    print "La suma es: ", calcula_suma(a,b)
    print "La resta es: ", calcula_resta(a,b)
    print "La division es: ", calcula_divicion(a,b)
    print "La multiplicacion es: ", calcula_multiplicacion(a,b)


calcula_operaciones_basicas(2,2)
