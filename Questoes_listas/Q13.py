"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média 
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

mes = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
       'Julho', 'Agosto', 'setembro', 'Outubro', 'novembro', 'Dezembro']
media = 0
lista_temperatura = []
for i in range(12):
    temperatura = float(input("Informe uma temperatura de %s :" % (mes[i])))
    lista_temperatura.append(temperatura)
    media += temperatura
media = media/12
for i in range(len(lista_temperatura)):
    if (lista_temperatura[i] > media):
        print("Em %s a temperatura foi %.2f... acima da media" %
              (mes[i], lista_temperatura[i]))
