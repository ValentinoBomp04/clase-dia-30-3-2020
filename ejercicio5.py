# encoding: utf-8
import sys

monto = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
duracion = int(input("¿Años?"))
for i in range(duracion):
    monto *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(monto, 2)))
