from src.contato import Contato
from src.identificador import Identificador


class Agenda:
    def __init__(self):
        self.agenda = {}

    def getContatos(self) -> list:
        retorno = []
        # for contato in self.agenda:
        #     temp[contato.getName()] = contato
        nomes = sorted(self.agenda)
        for ordenado in nomes:
            retorno.append(self.agenda.get(ordenado))
        return retorno

    def getQuantidadeDeContatos(self) -> int:
        return len(self.agenda)

    def getContato(self, nome: str) -> Contato:
        if nome in self.agenda:
            return self.agenda[nome]
        else:
            return None
            # Não encontrado

    def adicionarContato(self, contato: Contato) -> bool:
        if contato.getQuantidadeFones() > 0:
            if contato.getName() in self.agenda:
                numero = self.agenda.get(contato.getName())
                lista = contato.getFones()
                for num in lista:
                    numero.adicionarFone(num)
                return False
            else:
                self.agenda[contato.getName()] = contato
                return True
        else:
            return False

    def removerContato(self, nome: str) -> bool:
        if nome in self.agenda:
            self.agenda.pop(nome)
            return True
        else:
            return False

    def removerFone(self, nome: str, index: int) -> bool:
        if nome in self.agenda:
             contato = self.agenda.get(nome)
             return contato.removerFone(index)
        else:
            return False

    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        qtd = 0
        for contato in self.agenda.values():
            qtd += contato.getQuantidadeDeFonesPorId(identificador)
        return qtd

    def getQuantidadeDeFones(self) -> int:
        qtd = int(0)
        for contato in self.agenda.values():
            print(contato)
            qtd += contato.getQuantidadeFones()
        return qtd

    def pesquisar(self, expressao: str) -> list:
        numero = any(char.isdigit() for char in expressao)
        if numero is False:
            x = self.pesquisaPorNome(expressao)
            return self.ordemAlfabetica(x)
        else:
            x = self.pesquisaPorNumero(expressao)
            return self.ordemAlfabetica(x)

    def pesquisaPorNome(self, expressao: str):
        lista = []
        for nome in list(self.agenda.keys()):
            N = len(expressao)
            for letras in range(len(nome)):
                if (len(nome) - letras) < len(expressao):
                    break
                else:
                    a = nome[letras:letras + N]
                    if a == expressao:
                        lista.append(nome)
                        break
        resultado = []
        for i in range(len(lista)):
            resultado.append(self.agenda.get(lista[i]))
        return resultado

    def pesquisaPorNumero(self, expressao: str):
        lista = []
        for nome in list(self.agenda.keys()):
            contatos = self.agenda.get(nome)
            test = False
            N = len(expressao)
            fones = contatos.getFones()
            for fone in fones:
                numero = fone.getNumero()
                for caracter in range(len(numero)):
                    if (len(numero) - caracter) < len(expressao):
                        break
                    else:
                        a = numero[caracter:caracter + N]
                        if a == expressao:
                            lista.append(nome)
                            test = True
                            break
                if test == True:
                    break
        resultado = []
        for i in range(len(lista)):
            resultado.append(self.agenda.get(lista[i]))
        return resultado

    def ordemAlfabetica(self, lista: list) -> list:
        retorno = []
        temp = {}
        for contato in lista:
            temp[contato.getName()] = contato
        nomes = sorted(temp)
        for ordenado in nomes:
            retorno.append(self.agenda.get(ordenado))
        return retorno
