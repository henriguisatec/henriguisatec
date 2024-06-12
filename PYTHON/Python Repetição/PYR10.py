#10) Escrever um algoritmo que leia os dados de "N" pessoas (nome, sexo(M/F)), idade e
#a saude numa escala de 0 a 10. Informe se está apto ou não para cumprir o serviço militar obrigatorio.
#Informe os totais. Uma pessoa está apta ao serviço militar obrigatorio se tiver uma saúde acima de 6, ter mais de 18 anos e ser do sexo M.

pessoas = int(input("Insira o número de pessoas: "))
for i in range (0,pessoas):
    if pessoas >= i:
        nome = str(input("Insira o nome: "))
        sexo = str(input("Insira seu sexo (M/F): "))
        idade = int(input("Insira sua idade: "))
        saude = int(input("Insira sua saúde em uma escala de 0 a 10: "))
        if saude>6 and idade>=18 and sexo == "m" or sexo == "M":
            print(f"{nome} está apto para entrar no exercito, parabéns soldado!")
        else:
            print(f"{nome} não está apto para entrar no exercito.")