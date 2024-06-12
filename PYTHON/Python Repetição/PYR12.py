'''
12) Escreva um algoritmo para calcular o fatorial do número N, cujo valor é obtido através
do usuário pelo teclado.
'''
numero = int(input("Insira um número inteiro: "))
if numero == 0:
    print("O fatorial é 1.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial*i
    print(f"O fatorial de {numero} é {fatorial}.")
