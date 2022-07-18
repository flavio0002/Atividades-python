"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram 
lidas. Imprima as consoantes."""
v = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
contc = 0  # Contador de consoantes
for x in v:
    if(x.upper() != "a" or x.upper() != "e" or x.upper() != "i" or x.upper() != "o" or x.upper() != "u"):
        contc += 1
print("No vetor existem %i consoantes" % (contc))
for x in v:
    if(x.upper() != "a" or x.upper() != "e" or x.upper() != "i" or x.upper() != "o" or x.upper() != "u"):
        print(x, end=" ")
print()
