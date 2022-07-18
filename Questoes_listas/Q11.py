"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for elemento in range(10):
    vetor1.append(int(input("Digite um elemento: ")))

for elemento in range(10):
    vetor2.append(int(input("Digite um elemento: ")))

for elemento in range(10):
    vetor3.append(int(input("Digite um elemento: ")))

for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print(vetor4)
