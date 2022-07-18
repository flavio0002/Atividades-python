"""Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada 
    ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela 
    deve crescer 0,5 cm. """


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if(self.idade < 21):
            self.altura += 0.05

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso += peso

    def crecer(self, altura):
        self.altura += altura


"""p = Pessoa("flavio", 20, 64, 1.73)
p.envelhecer()
print(p.idade)
print(p.altura)"""
