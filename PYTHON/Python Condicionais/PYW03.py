#3. Construa um algoritmo que leia dois valores númericos inteiros e efetue a adição; caso o resultado seja maior que 10, apresenta-lo.

numb1 = int(input("Insira o primeiro número inteiro: "))
numb2 = int(input("Insira o segundo número inteiro: "))
sum = numb1 + numb2
if sum>10:
    print(("O valor é maior que dez, o resultado é {}.").format(sum))
else:
    print("O valor da soma não é maior que dez.")

