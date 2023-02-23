class Pessoa:
    def __init__(self, id):
        self.id = id
        self.nome = None
    
    @property
    def ___nome_(self):
        return self.__nome

    @___nome_.setter
    def ___nome_(self, __nome):
        self.__nome = __nome
