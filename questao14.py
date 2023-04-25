numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

numeros.sort(reverse=True)

print("Lista em ordem decrescente:")
for numero in numeros:
    print(numero, end=" ")
