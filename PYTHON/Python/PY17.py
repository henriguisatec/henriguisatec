#17. A padaria Pão&Bão tem um fluxo diário de vendas de pães franceses e broas. Cada
#pão é vendido por R$ 0,12 e cada broa por R$ 1,50. No final de cada dia, o
#proprietário deseja saber quanto foi arrecadado com a venda total de pães e broas e
#quanto ele deve guardar em uma conta poupança, correspondente a 10% desse valor
#arrecadado. Para ajudar o proprietário, você foi contratado para fazer os cálculos. Faça
#um algoritmo para ler as quantidades de pães e de broas, e depois efetue o cálculo.

paes = int(input("Insira a quantidade de pães vendidos: "))
broa = int(input("Agora, quantas broas foram vendidas: "))
valorpao = paes*0.12
valorbroa = broa*1.50
valordia = valorpao+valorbroa
print(("O valor de vendas do dia foi de: {}R$").format(valordia))

poup = valordia*0.10
rounded = (round(poup,2))
print(("O valor destinado a poupança é de: {}R$").format(rounded))