primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

primeirosNomes = list(enumerate(primeirosNomes))
sobreNomes = list(enumerate(sobreNomes))
idades = list(enumerate(idades))

for i in range(4):
    print(f'{i} - {primeirosNomes[i][1]} {sobreNomes[i][1]} está com {idades[i][1]} anos')