#5. Construa um algoritmo que determine se um dado número inteiro é PAR OU IMPAR.

numb = int(input("Insira um número inteiro: "))
rest = numb%2
if rest==0:
    print("O número é par. Parabéns!")
else:
    print("O número é ìmpar. Que pena.")