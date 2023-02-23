b = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
def duplicate(lista):
    return list(set(lista))

print(duplicate(b))