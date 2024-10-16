import random

numero_1 = 5
numero_2 = 2

def sumatoria(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma

print(sumatoria(numero_1, numero_2))


def primer_vocal_palabra(palabra):

    palabra = "hola"
    vocales = "aeiou"
    contador = 0
    primer_vocal = " "

    for i in palabra:
        if i in vocales and contador == 0:
            contador +=1
            primer_vocal = i


print(primer_vocal_palabra(palabra))

palabra = " casa"

def obtener_consonantes(palabra):
    vocales = "aeiou"
    consonantes = ""

    for letra in palabra:
        if letra not in vocales:
            consonantes += letra

    return consonantes

print(obtener_consonantes(palabra))




def num_azar(cantidad, inicio, fin):

    azar = " "

    for i in range(cantidad):

        azar += str(random.randint(inicio, fin))
    return azar
cantidad = 4
inicio = 6
fin = 9

print(num_azar(cantidad, inicio, fin))




def divisores(numero):

    lista = []

    for i in range(1, numero+1):
        if numero % i == 0:
            lista.append(i)
    return lista






numero  = 7

def es_primo(numero):
    return len(divisores(numero)) == 2







