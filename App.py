import tkinter as tk
from tkinter import scrolledtext, font
import networkx as nx
import matplotlib.pyplot as plt

from BuscaTopologica import Grafo, OrdenacaoTopologica


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Busca Topológica")
        self.master.geometry("700x600")
        self.master.configure(bg="#2E3440")

        self.grafo = Grafo()
        self.ordenacao = OrdenacaoTopologica(self.grafo)

        self.fonte_titulo = font.Font(family="Helvetica", size=16, weight="bold")
        self.fonte_texto = font.Font(family="Consolas", size=12)

        self.label = tk.Label(master, text="Ordenacao Topologica das Disciplinas",
                              bg="#2E3440", fg="#D8DEE9", font=self.fonte_titulo)
        self.label.pack(pady=(20, 10))

        self.btn_ordenar = tk.Button(master, text="Executar Ordenacao e Mostrar Grafo", command=self.executar_ordenacao,
                                     bg="#81A1C1", fg="#2E3440", font=self.fonte_texto,
                                     activebackground="#5E81AC", activeforeground="#ECEFF4",
                                     relief=tk.RAISED, bd=3, padx=10, pady=5)
        self.btn_ordenar.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, width=80, height=20,
                                                   font=self.fonte_texto, bg="#3B4252", fg="#ECEFF4",
                                                   relief=tk.SUNKEN, bd=2)
        self.text_area.pack(pady=10, padx=10)

    def executar_ordenacao(self):
        self.text_area.delete('1.0', tk.END)
        ordem = self.ordenacao.ordenar()
        for i, disciplina in enumerate(ordem, 1):
            self.text_area.insert(tk.END, f"{i} - {disciplina}\n")

        self.mostrar_grafo()

    def mostrar_grafo(self):
        G = nx.DiGraph()

        for vertice in self.grafo.vertices.values():
            G.add_node(vertice.rotulo)

        for vertice in self.grafo.vertices.values():
            for adjacente in vertice.adjacentes:
                G.add_edge(vertice.rotulo, adjacente.vertice.rotulo)

        plt.figure(figsize=(20, 15))
        pos = nx.spring_layout(G, seed=42, k=1.2) 
        nx.draw(G, pos, with_labels=True, node_color="#81A1C1", edge_color="#D8DEE9",
                node_size=2000, font_size=10, font_weight="bold", arrowsize=20)
        plt.title("Grafo Direcionado das Disciplinas", fontsize=16)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

