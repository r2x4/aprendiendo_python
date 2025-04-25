def potencia (base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
base = int(input('Base Potencia: '))
exponente = int(input('Exponente Potencia: '))
print(f'{base} elevado a {exponente} es {potencia(base, exponente)}')

def tabla(n):
    for i in range(1, 11):
        print(f'{n} X {i} = {n*i}')
n = int(input('Ingresa numero para tabla multiplicacion: '))
tabla(n)