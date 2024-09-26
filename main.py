#Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
#a) a soma total entre eles
#b) a soma dos que forem pares.
#c) a soma dos que forem ímpares


numeros = list(map(int, input("Digite os numeros separados por virgula: ").split(',')))

print(f"\nA soma dos numeros eh igual a: {sum(numeros)}")

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        add_par = pares.append(num)
    elif num % 2 != 0:
        add_impar = impares.append(num)
    else:
        print("Invalido!")


soma_pares = sum(pares)
soma_impares = sum(impares)

print(f"\nA soma dos impares eh igual a: {soma_impares}")
print(f"\nA soma dos pares eh igual a: {soma_pares}")