from transformer import transformer
def find_values(lista):
    index = 1
    new_list = []
    for i in lista:
        new_list.append(i[4])
    new_list = sorted(new_list)
    count_dict = {}
    
    for i in range (len(new_list)-1):
        if new_list[i] == new_list[i + 1]:
            index+=1
        else:
            count_dict[new_list[i]] = index
            index = 1
    count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    count_dict = dict(count_dict)
    first_to_5 = {k: count_dict[k] for k in list(count_dict)[:5]}
    return first_to_5

files = transformer("atores/actors.csv")
files = find_values(files)
print("5 filmes com maior frequência:")
for key in files:
    print(f'{key}: {files[key]} filmes')