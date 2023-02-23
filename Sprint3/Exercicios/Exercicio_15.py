class Lampada:
    def __init__(self,args):
        self.ligada = False
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada