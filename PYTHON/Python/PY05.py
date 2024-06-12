#5) Faça um algoritmo que leia o valor do salário minimo e o valor de salario de um usúario de um usuario, calcule quantos salarios minimos esse ususario ganha e imprima na tela o resultado (1.293,20)

sala = float(input("Insira o valor do salário: "))
malekum = float(input("Insira o salário minimo: "))

output = sala / malekum
rounded = round(output, 2)
print(("Você ganha {} salários minimos").format(rounded))