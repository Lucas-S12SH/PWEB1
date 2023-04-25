numero = int(input("Digite um número inteiro: "))+1

fibonacci = [0, 1]

while fibonacci[-1] < numero:
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print("Sequência de Fibonacci até", numero, ":")
for numero_fibonacci in fibonacci:
    if numero_fibonacci <= numero:
        print(numero_fibonacci, end=" ")