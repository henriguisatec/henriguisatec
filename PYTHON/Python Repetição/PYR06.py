#6) Criar um algoritmo que leia um número(NUM), e depois leia NUM números inteiros e imprima o maior deles.

num = int(input("Informe o número de repetições: "))
if num<=0:
    print("Número invalido.")
maior = 0
for i in range(1,num+1):
    n = int(input(f"Informe o {i} número: "))

    if i == 1:
        maior = n

    if n > maior:
        maior = n

print(maior)