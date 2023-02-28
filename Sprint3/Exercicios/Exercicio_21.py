class Passaro:
    def __init__(self):
        self.nome = None

    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        pass
    
class Pato(Passaro):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        self.nome = "Pato"
        print("{self.nome} emitindo som..."+ "\n" + "Quack Quack")

class Pardal(Passaro):
    def __init__(self ):
        super().__init__()
    
    def emitir_som(self):
        self.nome = "Pardal"
        print("{self.nome} emitindo som..." + "\n" + "Piu Piu")
    


