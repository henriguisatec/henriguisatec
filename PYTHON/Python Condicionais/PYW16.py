'''
16. Escrever um algoritmo que leia três valores inteiros distintos e os escreva em ordem
crescente.
'''

#lista = [nu1, nu2, nu3]
#lista_ordem = sorted(lista)
#print(lista_ordem)

primeiro = int(input("Insira um número inteiro: "))
segundo = int(input("Insira um segundo número inteiro: "))
terceiro = int(input("Insira um terceiro número inteiro: "))

if primeiro<segundo<terceiro:
    print("A ordem crescente é:" ,primeiro, segundo, terceiro)
elif primeiro<terceiro<segundo:
    print("A ordem crescente é:" ,primeiro, terceiro, segundo)
elif segundo<primeiro<terceiro:
    print("A ordem crescente é:" ,segundo, primeiro, terceiro)
elif segundo<terceiro<primeiro:
    print("A ordem crescente é:" ,segundo, terceiro, primeiro)
elif terceiro<primeiro<segundo: 
    print("A ordem crescente é:" ,terceiro, primeiro, segundo)
elif terceiro<segundo<primeiro:
    print("A ordem crescente é:" ,terceiro, segundo, primeiro)

