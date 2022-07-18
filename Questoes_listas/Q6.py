"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""
v = []
for i in range(10):
    media = 0
    print("Nota %iº aluno" % (i+1))
    for x in range(4):
        media += float(input("Insira a %iº nota: " % (x+1)))
    v.append(media/4)
for i in range(10):
    if(v[i] >= 7):
        print("Aluno: ", (i+1))
        print("media", media)
