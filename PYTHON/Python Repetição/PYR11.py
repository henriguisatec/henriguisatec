#11) Faça um algoritmo que receba "N" e mostre positivo, negativo ou zero para cada número.

n = int(input("Insira quantos números você deseja para analize: "))
if n <= 0:
    print("O número que você digitou é invalido.")
for i in range (0,n):
    numb = int(input("Insira o número para analize: "))
    if numb>0:
        (print(f"O número {numb} é positivo."))
    elif numb<0:
        (print(f"O número {numb} é negativo."))
    else:
        print("O número é zero.")