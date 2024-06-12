'''
13. A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários.
O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Fazer um
algoritmo que permita entrar com o salário bruto e o valor da prestação, e informar se
o empréstimo pode ou não ser concedido.
'''

salary = float(input("Insira seu salário bruto: "))
prest = float(input("Insira o valor da prestação: "))
thirty = (salary*0.3)
#print(thirty)
if prest>thirty:
    print("O emprestimo não pode ser realizado.")
else:
    print("O emprestimo pode ser realizado.")