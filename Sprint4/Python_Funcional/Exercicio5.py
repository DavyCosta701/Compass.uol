import csv
lista = {}

with open('estudantes.csv', encoding='utf8') as f:
    freader = csv.reader(f, delimiter=',')
    lista = {x[0]: x[1:] for x in freader}

dicio = sorted(lista.items())



lista2 = [x[1][:] for x in dicio]
lista3 = []
lista4 = [x[0] for x in dicio]
lista5 = []


for i in lista2:
    lista3.append(list(map(int, i)))

for i in lista3:
    lista5.append(sorted(i, reverse=True))



for i in range(len(lista3)):
    print(f'Nome: {lista4[i]} Notas: {sorted(lista5[i][0:3],reverse=True)} Média: {round(sum(lista5[i][0:3])/3,2)}') 




    