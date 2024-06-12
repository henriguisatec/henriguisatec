'''
8. Escreva um algoritmo em PORTUGOL que leia um número e imprima a raiz quadrada
do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja
negativo.
'''

numero = int(input("Insira um número para ser analisado: "))
if numero>=0:
    raiz = numero**(1/2)
    print("Número positivo, logo:" ,raiz)

else:
    pot = numero**2
    print("O número é negativo, logo:" ,pot)
