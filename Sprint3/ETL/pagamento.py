from transformer import transformer
def find_values(lista):
    index = 1
    count_dict = {lista[0]: lista[5] for lista in lista}
    count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    count_dict = dict(count_dict)
    return count_dict

files = transformer("atores/actors.csv")
files = find_values(files)
for i in files.keys():
    print(f'{i}: {files[i]}')