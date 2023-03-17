def conta_vogais(string):
    lista_letras = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(string)):
        lista_letras.append(string[i])
    
    lista_vogais = list(filter(lambda x: x in vowels, lista_letras))
    return len(lista_vogais)





    
