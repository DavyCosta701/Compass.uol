def reducer(arg):
    lista = arg.split(',')
    lista = list(map(lambda x: int(x),lista))
    var = 0
    for i in lista:
        var+=i
    return var
a = "1,3,4,6,10,76"
var = reducer(a)
print(var)