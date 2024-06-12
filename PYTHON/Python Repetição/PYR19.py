'''
19) Considere:
H = 1 - 1/2 + 1/3 - 1/4 + ... 1/N
faça um algoritmo para gerar o número H. O número N é lido do teclado.
'''

ene = int(input("Insira o valor de N: "))

print("H = 1",end=" ")
for h in range (2,ene+1):
    if h % 2 == 0:
        print(f"- 1/{h}", end=" ")
    else:
        print(f"+ 1/{h}", end=" ")

H = float(1)

print("H = 1", end=" ")
for h in range(2, ene + 1):
    if h % 2 == 0: 
        H -= 1 / h 
        print(f"- 1/{h}", end=" ")
    else:
        H += 1 / h 
        print(f"+ 1/{h}", end=" ")

print(f"\nO valor de H é: {H}")