'''
20. Faça um algoritmo que calcule o valor da conta de luz de uma pessoa. Sabe-se que o
cálculo da conta de luz segue a tabela abaixo:
Tipo de Cliente - Valor do KW/h
1 (Residência) - 0,60
2 (Comércio) - 0,48
3 (Indústria) - 1,29
'''

print("TIPOS DE CLIENTE.")
print("1 - (Residência) - 0,60")
print("2 - (Comércio) - 0,48")
print("3 - (Indústria) - 1,29")
tipo = int(input("Insira o tipo de cliente desejado (1,2,3): "))
if tipo == 1:
    voltagem = float(input("Insira a quantidade de KW/h ultilizados na residência: "))
    conta = voltagem*0.60
    print("A valor da conta do cliente é:",conta)
if tipo == 2:
    voltagem = float(input("Insira a quantidade de KW/h ultilizados no ponto comercial: "))
    conta = voltagem*0.48
    print("A valor da conta do cliente é:",conta)
if tipo == 3:
    voltagem = float(input("Insira a quantidade de KW/h ultilizados na indústria: "))
    conta = voltagem*1.29
    print("O valor da conta do cliente é:",conta)