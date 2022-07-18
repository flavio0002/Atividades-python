import math

tamanho_metros = float(input("Informe o tamanho em metros quadrados a ser pintado: "))
litros = (tamanho_metros/3)
latas = math.ceil(litros/18)

print("A quantidade de lata de tinta a ser comprada é %.2f" % (latas))
print("Valor Total: %.2f R$" % math.ceil(latas*80))