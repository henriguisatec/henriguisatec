#Calculadora

#defs

def menu():
    print("Bem vindo ao app da calculadora!")
    print("Opções possiveis:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("6. Raiz Quadrada")
    print("7. Porcentagem")
    print("8. Resto da divisão")
    print("9. Divisão por inteiro")
    print("10. Sair do programa")
    opera = int(input("Qual operação você deseja?: "))
    return opera

def soma():
    a = int(input("Insira um número inteiro: "))
    b = int(input("Insira outro número inteiro: "))
    soma = a+b
    print(" ")
    print((f"{a} + {b} = {soma}"))
    print(" ")

def sub(): 
    a = int(input("Insira um número inteiro: "))
    b = int(input("Insira outro número inteiro: "))
    sub = a-b
    print(" ")
    print((f"{a} - {b} = {sub}"))
    print(" ")

def multi():
    a = int(input("Insira um número inteiro: "))
    f = int(input("Insira outro número inteiro: "))
    multi = a*f
    print(" ")
    print((f"{a} x {f} = {multi}"))
    print(" ")

def div():
    g = int(input("Insira um número inteiro: "))
    h = int(input("Insira outro número inteiro: "))
    if g or h == 0: #
        print(" ")
        print((f"{g} / {h} = 0"))
        print(" ")
    else:
        div = g/h
        print(" ")
        print((f"{g} / {h} = {float(round(div, 2))}"))
        print(" ")

def expo():
    i = int(input("Insira um número inteiro: "))
    j = int(input("Insira outro número inteiro: "))
    expo = i**j
    print(" ")
    print((f"{i} ^ {j} = {expo}"))
    print(" ")

def root():
    l = int(input("Insira um número inteiro: "))
    root = l**0.5
    print(" ")
    print((f"{l}# = {float(round(root, 2))}"))
    print(" ")

def porcen():
    m = int(input("Insira o percentual inteiro: "))
    numero = int(input("Insira um valor para ser acrescentado o percentual: "))
    porcentagem = m/100*numero
    print(" ")
    print((f"{m}% de {numero } = {porcentagem}"))
    print(" ")

def resto():
    o = int(input("Insira um número inteiro: "))
    n = int(input("Insira outro número inteiro: "))
    if o or n == 0:
        print(" ")
        print((f"{o} / {n} = 0"))
        print(" ")
    else:
        resto = o%n  ######
        print(" ")
        print((f"{o} / {n} = {resto}"))
        print(" ")

def inteiro():
    p = int(input("Insira um número inteiro: "))
    q = int(input("Insira um número inteiro: "))
    inteiro = p//q
    print(" ")
    print((f"{p} / {q} = {inteiro}"))
    print(" ")

while exit!=10:
    opera = menu()
    if opera == 1:
        soma()
    elif opera == 2:
        sub()
    elif opera == 3:
        multi()
    elif opera == 4:
        div()
    elif opera == 5:
        expo()
    elif opera == 6:
        root()
    elif opera == 7:
        porcen()
    elif opera == 8:
        resto()
    elif opera == 9:
        inteiro()
    elif opera == 10:
        print("Fechando o programa...")
        exit = 10
    elif opera > 10 or opera < 1:
        print(" ")
        print("O número não é valido.")
        print(" ")
    
    