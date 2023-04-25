numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

soma = sum(numeros)
media = soma / len(numeros)

print("A média dos números é:", media)
