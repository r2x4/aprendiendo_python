# funciones
# ejercicion 1

def area_circulo(radio: float) -> float:
    pi = 3.1416
    return pi * radio ** 2

print(area_circulo(3.6))

# ejercicio 2

def es_par(numero):
    return numero % 2 == 0

numero = int(input('Ingresa un número: '))
if es_par(numero):
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')

# ejercicio 3

def suma_lista(lista):
    return sum(lista)

lista = []

cantidad = int(input('Cuantos numeros vas a ingresar: '))

for _ in range(cantidad):
    numero = int(input('Ingresa numero: '))
    lista.append(numero)
print(f'La suma de la lista es: {suma_lista(lista)}')



