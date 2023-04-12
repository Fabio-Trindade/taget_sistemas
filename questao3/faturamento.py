import json

def jsonFaturamentoToListInt(nomeArquivo:str):
    lista = []
    with open (nomeArquivo) as arquivo:
        faturamentos = json.load(arquivo)
        for faturamento in faturamentos:
            lista.append(faturamento['valor'])
    return lista

class Faturamento:
    def __init__(self,faturamentos):
        self._faturamentos = faturamentos
    
    def getMenorFaturamento(self)-> int:
        menorValor = self._faturamentos[0]
        for valor in self._faturamentos[1:]:
            if valor < menorValor:
                menorValor = valor
        return menorValor
    
    def getMenorFaturamentoNaoNulo(self)-> int:
        menorValor = self._faturamentos[0]
        for valor in self._faturamentos[1:]:
            if valor!=0:
                if menorValor == 0:
                    menorValor = valor
                elif valor < menorValor:
                    menorValor = valor
        return menorValor
    
    def getMaiorFaturamento(self)-> int:
        maiorValor = self._faturamentos[0]
        for valor in self._faturamentos[1:]:
            if valor > maiorValor:
                maiorValor = valor
        return maiorValor
    
    def getMediaFaturamento(self) -> int:
        dias = 0
        somaFaturamento = 0
        for faturamento in self._faturamentos:
            if faturamento!=0:
                somaFaturamento += faturamento
                dias+=1
        return somaFaturamento/dias

    def getQtdDiasFaturamentoMaiorMedia(self)->int:
        dias = 0
        media = self.getMediaFaturamento()
        for faturamento in self._faturamentos:
            if faturamento >= media:
                dias+=1
        return dias
    
    def imprimirInfosFaturamento(self):
        print("Menor faturamento do mês: R$",self.getMenorFaturamento())
        print("Menor faturamento não nulo do mês: R$",self.getMenorFaturamentoNaoNulo())
        print("Maior faturamento do mês: R$",self.getMaiorFaturamento())
        print("Média do faturamento do mês:R$",self.getMediaFaturamento())
        print("Quantidade de dias em que o faturamento diário foi maior que a média mensal:",self.getQtdDiasFaturamentoMaiorMedia())

if __name__ == "__main__":
    lista = jsonFaturamentoToListInt("questao3/faturamento.json")
    faturamento = Faturamento(lista)
    faturamento.imprimirInfosFaturamento()