""" 
Ejercicio 1.6. Escribir funciones que resuelvan los siguientes problemas:
a) Dados dos numeros, imprimir la suma, resta, division y multiplicacion de ambos.
b) Dado un numero entero n, imprimir su tabla de multiplicar.
 """
#b

def imprime_tabla_multiplicar(numero):
    print '*****************************'
    print 'La tabla  multiplicar de  {} :'.format(numero)
    print '*****************************'
    for i in range(1,11):
        print '{} * {} ='.format(numero,i),i*numero

imprime_tabla_multiplicar(2)