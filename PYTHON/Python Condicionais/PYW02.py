#2. Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior.

numb1 = int(input("Insira o primeiro número inteiro: "))
numb2 = int(input("Insira o segundo número inteiro: "))
if numb1>numb2:
    print(("O número {} é o maior").format(numb1))
else:
    print(("O número {} é o maior").format(numb2))
