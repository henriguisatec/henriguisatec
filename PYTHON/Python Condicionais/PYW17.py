'''
17. Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os
lados de um triângulo. Se forem, informar qual o tipo de triângulo que eles formam:
equilátero, isóscele ou escaleno.

Propriedade: o comprimento de cada lado de um triângulo é menor do que a soma dos
comprimentos dos outros dois lados.

Triângulo Equilátero: aquele que tem os comprimentos dos três lados iguais;

Triângulo Isóscele: aquele que tem os comprimentos de dois lados iguais. Portanto,
todo triângulo equilátero é também isóscele;

Triângulo Escaleno: aquele que tem os comprimentos de seus três lados diferentes.
'''

n1 = int(input("Insira um lado: "))
n2 = int(input("Insira outro lado: "))
n3 = int(input("Insira outro lado: "))

if n1 < n2+n3 or n2 < n1+n3 or n3 < n1+n2:
    print("Os valores inseridos podem ser lados de um triangulo.")
    if n1==n2==n3:
        print("O triangulo é Equilátero, possui todos os lados iguais.")
    elif n1==n2 or n1==n3 or n2==n3:
        print("O triangulo é Isóceles, possui pelo menos dois lados iguais.")
    else:
        print("O triangulo é Escaleno, todos os lados são diferentes")
else:
    print("Não são lados de um triangulo.")
