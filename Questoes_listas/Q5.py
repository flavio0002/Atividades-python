"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os 
números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""
x = 0
v = []
v_par = []
v_impar = []
while(x < 20):
    nota = float(input("Digite uma nota: "))
    x += 1
    v.append(nota)
    if(nota % 2 == 0):
        v_par.append(nota)
    else:
        v_impar.append(nota)

print(v)
print(v_par)
print(v_impar)
