'''
16) Escreva um algoritmo que calcule o resto da divisão de A por B (número inteiros e
positivos), ou seja, A mod B, através de subtrações sucessivas. Esses dois valores são
passados pelo usuário através do teclado.
'''

x = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))

a = x

while a >= b:
    a = a - b

resto = a

print(f"O resto da divisão de {x} por {b} em subtrações sucessivas é {resto}")