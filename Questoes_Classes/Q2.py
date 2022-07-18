"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
from typing_extensions import Self


class Quadrado:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_base(self, base):
        self.base = base

    def mudar_base(self, altura):
        self.altura = altura

    def retornar_base(self):
        return self.base

    def retornar_altura(self):
        return self.altura

    def calcular_area(self):
        return (self.base*self.altura)
