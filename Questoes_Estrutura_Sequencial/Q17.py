"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em
    3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%
    de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. """
tam_metros = float(input("Informe o tamanho em (metros) a ser pintado: "))
print("Latas de 18: ")
litros = tam_metros/6
quantidade_litros = (litros/18)
valor_litros = quantidade_litros*80

print("A quantidade de tinta a ser comprada é %.0f litros" %
      (round(quantidade_litros)))
print("Preço %.2f R$" % round((valor_litros)))
quantidade_galoes = (litros/3.6)
valor_galoes = quantidade_galoes*25
print("Galões de 3,6: ")
print("A quantidade de tinta a ser comprada é %.0f galões" %
      (round(quantidade_galoes)))
print("Preço %.2f R$" % round(valor_galoes))

mistura_lata = quantidade_litros
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1
print('Mistura: %d latas e %d galões = %.2f' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
