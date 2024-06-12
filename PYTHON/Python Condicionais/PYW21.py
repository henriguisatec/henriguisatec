'''
21. Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e
ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70
anos podem adquirir apólices de seguro. Quanto às classes de ocupações, foram
definidos três grupos de risco. A tabela abaixo fornece as categorias em função da
faixa etária e do grupo de risco. Dados nome, idade e grupo de risco, determinar a
categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a
categoria do pretendente, e , caso a idade não esteja na faixa necessária, imprimir uma
mensagem.
'''
print("Bem vindo a companhia de seguros.")
nome = str(input("Insira seu nome: "))
grupo = str(input("Insira seu grupo de risco (Baixo, Médio, Alto): "))
idade = int(input("Insira sua idade para verificarmos se você se enquadra: "))

if idade < 17 or idade > 70:
    print("Desculpe, você não está na faixa etária permitida para adquirir uma apólice.")
else:
    if idade <= 20:
        if grupo == "Baixo":
            classe = 1
        elif grupo == "Médio":
            classe = 2
        else:
            classe = 3
    elif idade <= 24:
        if grupo == "Baixo":
            classe = 2
        elif grupo == "Médio":
            classe = 3
        else:
            classe = 4
    elif idade <= 34:
        if grupo == "Baixo":
            classe = 3
        elif grupo == "Médio":
            classe = 4
        else:
            classe = 5
    elif idade <= 64:
        if grupo == "Baixo":
            classe = 4
        elif grupo == "Médio":
            classe = 5
        else:
            classe = 6
    else:
        if grupo == "Baixo":
            classe = 7
        elif grupo == "Médio":
            classe = 8
        else:
            classe = 9

    print(f"Sua classe de ocupação no seguro é: {classe}.")
    print(f"Nome: {nome}, Grupo de risco: {grupo}, Classe de ocupação: {classe}")
