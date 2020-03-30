# encoding: utf-8
import sys

numero = int(input("Introduce la altura del triángulo que sea entero positivo: "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")
