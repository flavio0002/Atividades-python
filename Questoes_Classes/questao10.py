"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel 
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. """


class BombaCombustivel:
    tipo_combustivel = ""
    valor_litro = 0.0
    quantidade_combustivel = 0.0

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor/self.valor_litro
        self.quantidade_combustivel = self.quantidade_combustivel-litros
        return "Foram colocados %.2f litros de combustivel " % (valor/self.valor_litro)

    def abastecer_por_litro(self, quantidade):
        self.quantidade_combustivel = self.quantidade_combustivel-quantidade
        return "O valor da quantidade de combustivel abastecida é %.2f" % (quantidade*self.valor_litro)

    def alterar_valor(self, valorNovo):
        self.valor_litro = valorNovo

    def alterar_combustivel(self, tipoCombustivel):
        self.tipo_combustivel = tipoCombustivel

    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade_combustivel += quantidade

    def __str__(self):
        return ":%s\n:%.2f\n:%.0f R$" % (self.tipo_combustivel, self.valor_litro, self.quantidade_combustivel)


c = BombaCombustivel("Aditivada", 7.49, 5000)
while(True):
    while(True):
        op = int(input("""
MENU:
1 - Abastecer veiculo por valor
2 - abastecer veiculo por quantidade de litros
3 - Alterar valor do combustivel
4 - Alterar combustivel
5 - Alterar quantidade de combustivel
0 - Sair
:"""))
        if(op == 1):
            c.abastecer_por_valor(
                float(input("Informe o valor que deseja abastecer: ")))
        elif(op == 2):
            c.abastecer_por_litro(
                float(input("Informe a quantidade de litros que deseja abastecer: ")))
        elif(op == 3):
            c.alterar_valor(
                float(input("Informe o novo valor do combustivel: ")))
        elif(op == 4):
            c.alterar_combustivel(
                input("Informe o novo tipo de combustivel: "))
        elif(op == 5):
            c.alterar_quantidade_combustivel(
                float(input("Informe a quantidade de combustivel que deseja acrecentar: ")))
        elif(op == 0):
            break
    print("INFORMAÇÕES DO COMBUSTIVEL")
    print(c)
    break
