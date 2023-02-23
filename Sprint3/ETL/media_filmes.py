from transformer import transformer
def show_avg(lista):
    list_mov = [int(i[2]) for i in lista]
    return sum(list_mov)/len(list_mov)
    


files = transformer(r"Sprint3\ETL\atores\actors.csv")
print(f"A média de filmes é: {show_avg(files)}")