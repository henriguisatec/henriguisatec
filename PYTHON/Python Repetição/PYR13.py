'''
13) Escreva um algoritmo que receba vários números e verifique se eles são ou não
quadrados perfeitos. O algoritmo termina a execução quando for digitado um número
menor ou igual a 0. (Um número é quadrado perfeito quando tem um número inteiro como
raiz quadrada.)
'''

n = int(input("Insira um número para verificação: "))

while n>=0:
    raiz = n**0.5
    if raiz == int(raiz):
        print("O número é um quadrado perfeito.")
        n=-1
    else:
        print("O número não é um quadrado perfeito.")
    n = int(input("Insira um número para verificação: "))

