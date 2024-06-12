#7. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de
#vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15%
#de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário
#no final do mês.

name = str(input("Insira seu nome: "))
salary = float(input("Insira seu salário fixo: "))
sales = float(input("Insira o seu total de vendas efetuadas, valor em dinheiro:"))
comis = salary+sales*0.15

print("O seu nome é: ",name)
print("O seu salário é: ",salary)
print("O salário no final do mês é: ",comis)