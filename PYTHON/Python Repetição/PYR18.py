'''
18) A série de Fibonacci é formada pela sequência:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Escreva um algoritmo que gere a série de FIBONACCI até o N-ésimo termo
'''

ene = int(input("Insira o valor de N: "))

if ene == 1:
    print(ene)
elif ene == 2:
    print(1)
    print(1)
    print(ene)
else:
    a = 1
    b = 1

    print(a)
    print(b)

    for i in range (3,ene+1):
        soma = a+b
        print(soma)
        if soma == ene or soma > ene:
            break

        a=b
        b=soma