# encoding: utf-8
import sys

palabra = str(input("Introduce una palabra: "))
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])
