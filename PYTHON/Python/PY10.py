#10. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a
#variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor
#da variável A. Apresentar os valores trocados.

a = int((input)("Insira o valor de A: "))
b = int((input)("Insira o valor de B: "))
reserva = a
a = b
b = reserva
print(("A variavel A agora possui valor de {}").format(a))
print(("E a variavel B possui o valor de {}").format(reserva))