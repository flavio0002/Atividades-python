"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma 
dos quadrados dos elementos do vetor."""

vetor_A = []

for i in range(10):
    vetor_A.append(int(input("Digite  um número para o vetor: ")))
soma = 0
for i in range(len(vetor_A)):
    soma = soma+(i**2)
print("A soma dos quadrado dos vetores é ", soma)
