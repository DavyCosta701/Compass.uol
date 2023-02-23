class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.cor = 'azul'
        self.velocidade_maxima = velocidade_maxima;
        self.modelo = modelo
        self.capacidade = capacidade
    

boeing = Aviao('BOIENG456', '1500 km/h' , 400 )
embraer = Aviao('Embraer Praetor 600', '863km/h', 14)
antonov = Aviao('Antonov An-2', '258 Km/h', 12)
avioes = []
avioes.append(boeing)
avioes.append(antonov)
avioes.append(antonov)

for i in avioes:
    print(f"O avião de modelo {i.modelo} possui uma velocidade máxima de {i.velocidade_maxima}, capacidade para {i.capacidade} passageiros e é da cor {i.cor}")