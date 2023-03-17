lista = []
lista2 = []
def par(x):
    if x>0:
        return x
    else:
        return 0

with open('number.txt', 'r') as f:
    for line in f:
        lista.append(int(line))

lista2 = list(map(par, lista))
lista2 = list(filter(lambda x: x%2==0, lista2))


def small(itera):
    sort = sorted(itera, reverse=True)
    return sort[:5]

resultado = small(lista2)
print(resultado)
print(sum(resultado)) 
