#8) Criar um número que leia um número (NUM), e depois leia NUM números e calcule a média de todos os números lidos.

num = int(input("Insira a quantidade de números: "))
if num<=0:
    print("O número é invalido.")
soma = 0
for i in range (1,num+1):
    n = int(input("Insira um número: "))

    if i == 1:
        soma = n
    if i >=num:
        soma = soma + n
media = soma/2
print(media)

