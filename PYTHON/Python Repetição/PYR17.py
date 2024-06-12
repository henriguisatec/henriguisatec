'''
17) Criar um algoritmo que leia um número(NUM), e utilizando o loop PARA,
verifique se esse numero é primo ou não.
'''

num = int(input("Insira um número inteiro: "))

if num > 1:
    primo = True
    for i in range(2, num): #divisivel por um e ele mesmo
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print(f"{num} não é um número primo.")
