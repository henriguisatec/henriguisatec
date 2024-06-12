'''
7. Construir um algoritmo em PORTUGOL que leia dois números e efetue a adição. Caso o
valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
caso o valor somado seja menor ou igual a 20, este deverá ser apresentado
subtraindo-se 5.
'''

numb1 = int(input("Insira um número: "))
numb2 = int(input("Insira outro número: "))
sum = numb1 + numb2

if sum>20: 
    eight = sum+8
    print(("O valor é maior que vinte, logo: {}").format(eight))

else:
    five = sum-5
    print(("O valor é menor ou igual a vinte, logo: {}").format(five))
