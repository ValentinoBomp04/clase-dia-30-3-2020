# encoding: utf-8
import sys

palabra = raw_input("Introduce una frase: ")
letra = raw_input("Introduce una letra: ")
contador = 0
for i in palabra:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, palabra))
