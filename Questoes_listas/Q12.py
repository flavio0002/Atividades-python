"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

lista_alunos = []
media = 0
cont = 0
for i in range(30):
    print("Aluno ", (i+1))
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe  a altura: "))
    media += altura
    lista_alunos.append([idade, altura])
media/2
for i in range(len(lista_alunos)):
    if(lista_alunos[i][1] < media and lista_alunos[i][0] > 13):
        cont += 1
print("Existem %i alunos com altura  menor que a media: " % (cont))
