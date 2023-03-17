def calcular_valor_maximo(operadores,operandos) -> float:
    zipado = list(zip(operadores, operandos))
    zips = list(map(lambda x: eval(str(x[1][0]) + x[0] + str(x[1][1])), zipado))
    return max(zips)
