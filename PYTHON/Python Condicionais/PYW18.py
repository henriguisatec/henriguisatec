'''
18. A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um
algoritmo que calcule e exiba o salário de um professor. Sabe-se que o valor da
hora/aula segue a tabela abaixo:
Professor Nível 1 R$12,00 por hora/aula
Professor Nível 2 R$17,00 por hora/aula
Professor Nível 3 R$25,00 por hora/aula
'''

print("Tabela de níveis:")
print("Professor Nível 1 R$12,00 por hora/aula")
print("Professor Nível 2 R$17,00 por hora/aula")
print("Professor Nível 3 R$25,00 por hora/aula")
nivel = (input("Qual o nivel do professor que você deseja calcular o salario: "))

n1 = 12.00
n2 = 17.00
n3 = 25.00

if nivel == "nivel 1" or nivel == "1":
    print("Opção nivel 1:")
    ha = float(input("Insira o número de horas-aula: "))
    salario = (ha*n1)
    print("O salário a ser para o professor é:", salario)
elif nivel == "nivel 2" or nivel == "2":
    print("Opção nivel 2:")
    ha = float(input("Insira o número de horas-aula: "))
    salario = (ha*n2)
    print("O salário a ser para o professor é:", salario)
elif nivel == "nivel 3" or nivel == "3":
    print("Opção nivel 3:")
    ha = float(input("Insira o número de horas-aula: "))
    salario = (ha*n3)
    print("O salário a ser pago ao professor é:", salario)
else:
    print("O Nível é invalido.")

