from transformer import transformer
def find_max(lista):
    max_value = 0
    index = 0
    for i in range(len(lista)):
         if int(lista[i][2]) > max_value:
            max_value = int(lista[i][2])
            index = i 
        
    return lista[index]

files = transformer(r"Sprint3\ETL\atores\actors.csv")

print(f"O ator com mais filmes é {find_max(files)[0]} com {find_max(files)[2]} filmes")