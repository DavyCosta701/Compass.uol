def palindrome(w):
    list1 = list(w)
    list2 = list1[::-1]
    return list1 == list2


a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 
for i in a:
    if palindrome(i):
        print(f"A palavra: {i} é um palíndromo")
    else:
        print(f"A palavra: {i} não é um palíndromo")