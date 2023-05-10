from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()} | Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        print(" > Desktop cadastrado.")
