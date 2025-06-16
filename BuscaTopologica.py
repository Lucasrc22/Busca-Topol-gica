
import matplotlib.pyplot as plt

from Pilhas import Pilha


class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)


class Adjacente:
    def __init__(self, vertice, custo=1):
        self.vertice = vertice
        self.custo = custo


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.dados_grafo = {
            "Fundamentos de Programacao": [],
            "Programacao Imperativa": ["Fundamentos de Programacao"],
            "Linguagem de Programacao Orientada a Objetos": ["Programacao Imperativa"],
            "Algoritmos e Estruturas de Dados": ["Programacao Imperativa"],
            "Engenharia de Software": ["Algoritmos e Estruturas de Dados"],
            "Analise e Projeto de Software": ["Engenharia de Software"],
            "Banco de Dados": ["Algoritmos e Estruturas de Dados"],
            "Matematica Discreta": [],
            "Teoria da Computacao": ["Matematica Discreta"],
            "Construcao de Compiladores": ["Teoria da Computacao"],
            "Calculo I": [],
            "Calculo II": ["Calculo I"],
            "Calculo III": ["Calculo II"],
            "Equações Diferenciais": ["Calculo III"],
            "Teoria dos Grafos": ["Matematica Discreta"],
            "Geometria Analitica": [],
            "Algebra Linear": [],
            "Calculo Numerico": ["Calculo II"],
            "Organizacao de Computadores": [],
            "Arquitetura de Computadores": ["Organizacao de Computadores"],
            "Redes de Computadores I": [],
            "Redes de Computadores II": ["Redes de Computadores I"],
            "Sistemas Operacionais": ["Arquitetura de Computadores"],
            "Sistemas Embarcados": ["Sistemas Operacionais"],
            "Inteligencia Artificial": ["Algoritmos e Estruturas de Dados"],
            "Aprendizagem de Máquina": ["Inteligencia Artificial"]
        }
        self.criar_vertices()
        self.adicionar_arestas()

    def criar_vertices(self):
        for nome in self.dados_grafo:
            self.vertices[nome] = Vertice(nome)

    def adicionar_arestas(self):
        for vertice, prereqs in self.dados_grafo.items():
            for prereq in prereqs:
                self.vertices[prereq].adiciona_adjacente(Adjacente(self.vertices[vertice]))


class OrdenacaoTopologica:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitados = set()
        self.pilha = Pilha(len(grafo.vertices))

    def dfs(self, vertice):
        self.visitados.add(vertice)
        for adjacente in vertice.adjacentes:
            if adjacente.vertice not in self.visitados:
                self.dfs(adjacente.vertice)
        self.pilha.empilhar(vertice)

    def ordenar(self):
        for rotulo, vertice in self.grafo.vertices.items():
            if vertice not in self.visitados:
                self.dfs(vertice)

        resultado = []
        while True:
            v = self.pilha.desempilhar()
            if v is None:
                break
            resultado.append(v.rotulo)
        return resultado