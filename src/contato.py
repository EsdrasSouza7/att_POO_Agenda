from src.fone import Fone
from src.identificador import Identificador

class Contato:

    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        return len(self.telefones)

    def getFones(self) -> list:
        return self.telefones

    def adicionarFone(self, fone: Fone) -> bool:
        if fone.validarNumero(fone.getNumero()):
            self.telefones.append(fone)
            return True
        else:
            return False

    def removerFone(self, index: int) -> bool:
        if len(self.telefones) >= index+1 and index >= 0:
            self.telefones.pop(index)
            return True
        else:
            return False

    def getQuantidadeDeFonesPorId(self, identificador: Identificador):
        qtd = 0
        for numeros in self.telefones:
            if numeros.identificador == identificador:
               qtd += 1
        return qtd
