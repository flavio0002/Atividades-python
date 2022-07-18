"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números."""


def soma_vetor(vetor):
    print("A soma é ", sum(vetor))


def mult_vetor(vetor):
    mult = 0
    for x in vetor:
        mult = mult*x
    print("A Multiplicação é ", mult)


def mostra_numeros(vetor):
    for i in vetor:
        print(i, end=" ")
    print()


vetor = [1, 2, 3, 4, 5]

soma_vetor(vetor)
mult_vetor(vetor)
mostra_numeros(vetor)
