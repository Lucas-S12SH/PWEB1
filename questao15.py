numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

x = int(input("Digite um número: "))

if x in numeros:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")