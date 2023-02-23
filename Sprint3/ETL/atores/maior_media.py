from transformer import transformer
def max_media(lista):
    max_value = 0
    index = 0
    for i in range(len(lista)):
         if float(lista[i][3]) > max_value:
            max_value = float(lista[i][3])
            index = i 
        
    return lista[index]

files = transformer("atores/actors.csv")
print(f"O ator com maior média por filme é de {max_media(files)[0]} com {max_media(files)[3]}pts")