""" 
Ejercicio 1.3. Escribir funciones que permitan:
- a) Calcular el perimetro de un rectangulo dada su base y su altura.
- b) Calcular el area de un rectangulo dada su base y su altura.
- c) Calcular el area de un rectangulo (alineado con los ejes x e y) dadas sus coordenadas
x1, x2, y1, y2.
- d) Calcular el perimetro de un circulo dado su radio.
- e) Calcular el area de un circulo dado su radio.
- f) Calcular el volumen de una esfera dado su radio.
- g) Dados los catetos de un triangulo rectangulo, calcular su hipotenusa.

 """
import math
from fractions import Fraction

 # a)
def perimetro_rectangulo(base,altura):
    return base*altura
 
 # b)
def area_rectangulo(base, altura):
    return base*altura

# c)
def area_rectangulo_by_coordenadas(x1, x2, y1, y2):
    base = x2 - x1
    altura = y2 - y1
    return area_rectangulo(base,altura)

# d)
def perimetro_circulo(radio):
    return 2*math.pi*radio

# e)
def area_circulo(radio):
    return math.pi * pow(radio,2) 

# f)
def volumen_esfera(radio):
    return Fraction(4, 3)*math.pi*pow(radio,3)

# g)
def calcula_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt( pow(cateto_a,2) + pow(cateto_b,2))
    return hipotenusa
