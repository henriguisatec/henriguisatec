#14. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem
#juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das
#prestações.

compra = float(input("Insira o valor da compra: "))
prest = compra/5
rounded = (round(prest, 2))
print(("O valor da suas prestações é de: {} reais").format(rounded))