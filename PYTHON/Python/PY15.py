#15. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de
#venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
#percentual informado pelo usuário.

custo = float(input("Insira o valor de custo do produto: "))
percet = float(input("Insira o valor de valorização: " ))
acrescimo = custo*(percet/100)
final = acrescimo + custo
rounded = (round(final,2))
print(("O valor de venda do produto é: {} reais.").format(rounded))