numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

maior_numero = numeros[0]
menor_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print("Maior número da lista:", maior_numero)
print("Menor número da lista:", menor_numero)
