numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
