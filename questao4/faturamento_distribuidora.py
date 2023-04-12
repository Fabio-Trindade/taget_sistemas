import json

def jsonFaturamentoToListDict(nomeArquivo:str):
    with open (nomeArquivo) as arquivo:
        faturamentos = json.load(arquivo)
    return faturamentos

class FaturamentoDistribuidora:
    def __init__(self,faturamentos):
        self._faturamentos = faturamentos
    
    def getFaturamentoTotal(self):
        soma = 0
        for valor in self._faturamentos:
            for k,v in valor.items():
                soma+=v
        return soma
    
    def getPercentualPorEstado(self):
        lista = []
        faturamentoTotal =  self.getFaturamentoTotal()
        for faturamento in self._faturamentos:
            for k,v in faturamento.items():
                lista.append({k:v/faturamentoTotal})
        return lista
    
    def imprimirPercentualPorEstado(self):
        faturamentoPercentual =  self.getPercentualPorEstado()
        for faturamento in faturamentoPercentual:
            for k,v in faturamento.items():
                print(f'O faturamento obtido por {k} teve uma representação de {v*100} %.')
        return lista


if __name__ == "__main__":
    lista = jsonFaturamentoToListDict("questao4/faturamento_distribuidora.json")
    faturamentoDistribuidora = FaturamentoDistribuidora(lista)
    faturamentoDistribuidora.imprimirPercentualPorEstado()
    



    