#desafio

numb = int(input("Insira um número inteiro: "))
numb2 = int(input("Insira outro número inteiro: "))
div = numb // numb2
rest = numb - div*numb2
print(("A sobra da divisão é: {}").format(rest))

print(("A sobra da divisão é: {}").format(numb%numb2))


