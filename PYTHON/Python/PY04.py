# 4) Faça um algortimo que receba um número inteiro e imprima na tela o seu antecessor e seu sucessor.

numb = int(input("Insira um número inteiro: "))
antec = (numb - 1)
print(("O antecessor do número é: {}").format(antec))
suck = (numb + 1)
print(("O sucessor do número é: {}").format(suck))