#19. Faça um algoritmo que calcule e imprima o gasto de uma viagem de carro de uma
#cidade a outra, sabendo que:
#a. o carro utilizado roda 15 Km com 1 litro de gasolina;
#b. o preço médio da gasolina é de R$5,30;
#c. o valor de cada pedágio é de R$8,00.

kilo = float(input("Insira a distância em kilometros do trajeto perorrido: "))
pedagio = int(input("Insira quantos pedagios foram encontrados no trajeto: "))
gas = kilo/15
gasto = round((gas*5.30)+(pedagio*8),2)
print("O custo da viagem foi de:" ,gasto)