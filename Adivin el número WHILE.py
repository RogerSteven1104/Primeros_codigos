
import random
# Ejercicio 1: Adivina el número
numero_ganador = random.randint(1,20)
numero = int(input("Adivina el número y gana!! Ingresa un número del 1 al 20: "))
while numero != numero_ganador:
    if numero > numero_ganador:
        print("Busca un numero menor")
    if numero < numero_ganador:
        print("Busca un numero mayor")
    numero = int(input("Ingrese otro numero"))
print("Ganaste!! Felicidades")