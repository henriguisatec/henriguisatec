'''
1. Escreva um algoritmo em PORTUGOL que leia um número e o imprima caso ele seja
maior que 20.
'''

num = int(input("Insira um número inteiro: "))

if num > 20:
    print(f"O número {num} é maior que vinte.")
elif num == 20:
    print("O número é igual a vinte.")
else:
    print("O número não é maior que vinte.")