class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        pass
    
class Pato(Passaro):
    def __init__(self):
        super().__init__()
        
    
    def emitir_som(self):
        print("Pato emitindo som..."+ "\n" + "Quack Quack")

class Pardal(Passaro):
    def __init__(self ):
        super().__init__()
    
    def emitir_som(self):
        print("Pardal emitindo som..." + "\n" + "Piu Piu")
