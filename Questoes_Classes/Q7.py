"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar 
Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, 
o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou 
seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação 
por que ela pode ser calculada a qualquer momento."""


class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = ""

    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade
