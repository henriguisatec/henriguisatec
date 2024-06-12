#Calculadora

while exit!=5:
    print("Bem vindo ao app da calculadora!")
    print("Opções possiveis:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair do programa")
    opera = str(input("Qual operação você deseja?: "))
    if opera == "Adição" or opera == "SOMA" or opera == "1" or opera == "+":
        a = int(input("Insira um número inteiro: "))
        b = int(input("Insira outro número inteiro: "))
        soma = a+b
        print(" ")
        print((f"{a} + {b} = {soma}"))
        print(" ")
    elif opera == "Subtração" or opera == "MENOS" or opera == "2" or opera == "-":
        c = int(input("Insira um número inteiro: "))
        d = int(input("Insira outro número inteiro: "))
        sub = c-d
        print(" ")
        print((f"{c} - {d} = {sub}"))
        print(" ")
    elif opera == "Multiplicação" or opera == "*" or opera == "x" or opera =="X" or opera == "3":
        e = int(input("Insira um número inteiro: "))
        f = int(input("Insira outro número inteiro: "))
        multi = e*f
        print(" ")
        print((f"{e} x {f} = {multi}"))
        print(" ")
    elif opera == "Divisão" or opera == "/" or opera == "divisão" or opera =="%" or opera == "4":
        g = int(input("Insira um número inteiro: "))
        h = int(input("Insira outro número inteiro: "))
        div = g/h
        print(" ")
        print((f"{g} / {h} = {float(round(div, 2))}"))
        print(" ")
    elif opera == "Sair" or opera == "5" or opera == "sair" or opera =="fechar" or opera == "Fechar":
        print("Fechando o programa...")
        exit = 5
    
    