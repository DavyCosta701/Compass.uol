class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    def ordenacaoDecrescente(self):
        desc = sorted(self.listaBaguncada)
        return desc[::-1]
