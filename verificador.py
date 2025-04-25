def mirar(numero):
    if numero <= 0:
        return False
    suma_digitos = sum(int(d) for d in str(abs(numero)))
    return  suma_digitos != 0 and numero % suma_digitos == 0

print(mirar(30))
print(mirar(22))

