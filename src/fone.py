from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        valido = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '-', '.']
        for n in numero:
            if n in valido:
                pass
            else:
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
