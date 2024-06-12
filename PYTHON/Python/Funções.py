def saudacoes():
    print("ola mundo!")
    a = int(input("Insira A: "))
    b = int(input("Insira B: "))
    soma = a+b
    print(soma)

saudacoes()

def saudacoes_fulano(nome):
    print(f'Ola, {nome}')

saudacoes_fulano('Henrique')
saudacoes_fulano('Leguiça')

def soma():
    #resultado = 
    return 10+10#resultado

res = soma()
print(f'10 + 10 = {res}')

def soma_dois_num(num1, num2):
    return num1 + num2
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
res2 = soma_dois_num(num1,num2)
print(res2)