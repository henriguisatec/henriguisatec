'''
15) Criar um algoritmo que calcule o M.M.C (mínimo múltiplo comum) entre dois
números lidos. (por exemplo: o M.M.C, entre 10 e 15 é 30)
'''

a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))

if a>b:
    maior = a
else:
    maior = b
mmc = maior

while mmc % a != 0 or mmc % b != 0:
    mmc = mmc + maior
print(f"O MMC de {a} e {b} é: {mmc}")