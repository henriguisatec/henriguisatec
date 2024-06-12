'''
11. Escreva um algoritmo em PORTUGOL para determinar se um número A é divisível
por um outro número B. Esses valores devem ser fornecidos pelo usuário.
'''

a = int(input("Insira um número para assumir o valor de A: "))
b = int(input("Agora, insira um número para assumir o valor de B: "))
if ((a%b)==0):
    print(f"O número {a} é divisivel pelo número {b}!")
else:
    print(f"O número {a} não é divisivel por {b}.")