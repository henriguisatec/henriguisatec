#16. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
#percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o
#custo de fábrica, e depois a percentagem do distribuidor sobre o resultado). Supondo
#que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um
#algoritmo que leia o custo de fábrica de um carro e informe o custo ao consumidor do
#mesmo.

fabrica = float(input("Insira o custo de fábrica do automóvel: "))
impost = fabrica*0.45
fabricaimpost = fabrica + impost
distrib = fabricaimpost*0.28
final = fabricaimpost + distrib
rounded = (round(final,3))
print(("O valor do automóvel é: {} R$").format(rounded))