# encoding: utf-8
import sys

numero = int(input("Introduce la altura del triángulo que sea entero positivo: "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
