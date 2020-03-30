# encoding: utf-8
import sys

numero = int(input("Introduce un número entero positivo: "))
for i in range(numero, -1, -1):
    print(i, end=", ")
