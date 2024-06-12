'''
12. Escreva um algoritmo em PORTUGOL que leia um número e informe se ele é divisível
por 3 e por 7.
'''

#numb = int(input("Insira um número inteiro: " ))
#if (((numb%3)==0) and ((numb%7)==0)):
#    print("O número é divisivel ambos por 3 e por 7.")
#else:
#    print("O número não é divisivel por 3 e 7.")

numb = int(input("Insira um número inteiro: " ))
if (((numb%21)==0)):
    print("O número é divisivel ambos por 3 e por 7.")
else:
    print("O número não é divisivel por 3 e 7.")