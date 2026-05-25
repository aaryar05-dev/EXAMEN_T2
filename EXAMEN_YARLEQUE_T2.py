import random

def buscar(arreglo, i, minimo, maximo):

    if i == len(arreglo):
        return minimo, maximo

    if arreglo[i] % 3 == 0:

        if minimo == -1 or arreglo[i] < minimo:
            minimo = arreglo[i]

        if maximo == -1 or arreglo[i] > maximo:
            maximo = arreglo[i]

    return buscar(arreglo, i + 1, minimo, maximo)


n = int(input("Ingrese el tamaño del arreglo: "))

arreglo = []

for i in range(n):
    numero = random.randint(10, 9999)
    arreglo.append(numero)

print("Números generados:")
print(arreglo)

minimo, maximo = buscar(arreglo, 0, -1, -1)

if minimo != -1:
    promedio = (minimo + maximo) / 2
    print("Menor múltiplo de 3:", minimo)
    print("Mayor múltiplo de 3:", maximo)
    print("Resultado =", promedio)
else:
    print("No existen múltiplos de 3")