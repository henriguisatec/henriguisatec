#9) Faça um algoritmo utilizando a estrutura de repetição que imprima a tabuada de um número informado pelo usúario.

num = int(input("Insira um número para exibir sua tabuada: "))
if num<=0:
    print("O número não possui uma tabuada definida.")
controle = 10
tot = 0
for i in range (0,controle+1):
    if i == 0:
        print(f"{num} x 0 = 0")

    if i < controle:
        tot = tot + num
        print(f"{num} x {i+1} = {tot}")
 