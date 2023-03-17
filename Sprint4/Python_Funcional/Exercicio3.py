import functools
def calcula_saldo(lancamentos) -> float:
    lista_pagamentos = list(map(lambda x: x[0]*-1 if x[1]=='D' else x[0], lancamentos))
    return functools.reduce(lambda x, y: x+y, lista_pagamentos)

