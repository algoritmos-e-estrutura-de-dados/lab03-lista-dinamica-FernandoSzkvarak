from node import Node


class Lista:
    inicio = None

    def init(self):
        self.inicio = None

    def adicionar(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)

        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)

    def show(self):
        aux = self.inicio
        print("[", end='')

        while (aux != None):
            print(f"{aux.valor}, ", end='')
            aux = aux.proximo

        print("]")

    def remover_um(self, valor):
        aux = self.inicio

        if aux == None:
          return

        if aux != None:
          if aux.valor == valor:
            self.inicio = self.proximo
            self = None