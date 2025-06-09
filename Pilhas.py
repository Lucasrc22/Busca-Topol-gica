import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=object)

    def __pilhaCheia(self):
        return self.__topo == self.__capacidade - 1

    def __pilhaVazia(self):
        return self.__topo == -1

    def empilhar(self, valor):
        if self.__pilhaCheia():
            print("A Pilha está cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilhaVazia():
            print("A Pilha está vazia")
            return None
        else:
            valor = self.__valores[self.__topo]
            self.__valores[self.__topo] = None
            self.__topo -= 1
            return valor

    def verTopo(self):
        if self.__pilhaVazia():
            return None
        return self.__valores[self.__topo]
