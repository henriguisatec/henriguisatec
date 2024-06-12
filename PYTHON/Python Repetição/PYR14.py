'''
14) Escreva um algoritmo que receba uma string e, utilizando o loop ENQUANTO,
inverta essa string.
'''
texto = ""

while texto != "sair":
    print(" ")
    texto=str(input("Insira uma palavra para ser invertida: "))
    tam = len(texto)

    if texto == "SAIR" or texto == "sair":
        print("Você saiu.")
    else:
        while tam>=1:
            print(texto[tam-1], end='')
            tam-=1