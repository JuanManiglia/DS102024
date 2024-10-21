def facto(numero:int)->int:
    resultado = 1
    for num in range(1,numero+1):
        resultado = resultado * num
    return resultado
print(facto(6))