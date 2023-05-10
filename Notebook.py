from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self._Notebook__tempoDeBateria}"

    def cadastrar(self):
        print(" > Notebook cadastrado...")