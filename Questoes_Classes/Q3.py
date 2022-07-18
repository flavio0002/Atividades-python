"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades 
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e 
de rodapés necessárias para o local."""


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def setBase(self, base):
        self.base = base

    def setAltura(self, altura):
        self.altura = altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def calcular_area(self):
        return (self.base*self.altura)

    def calcular_perimetro(self):
        return self.base + self.base + self.altura + self.altura
