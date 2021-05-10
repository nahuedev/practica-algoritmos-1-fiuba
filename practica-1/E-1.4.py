# Ejercicio 1.5. Escribir una funcion que, dado un numero entero n, permita calcular su factorial.

def calcula_factorial(numero):
    total_factorial=1
    i=1
    for i in range(1,numero+1):
        total_factorial=total_factorial * i
    return total_factorial


print calcula_factorial(10)