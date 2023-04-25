numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

soma = 0
for numero in numeros:
    soma += numero

print("A soma dos números é:", soma)
