'''
20) Implementar um algoritmo para calcular o sen(X). O valor de X deverá ser digitado
em graus. O valor do seno de X será calculado pela soma dos 15 primeiros termos da série
a seguir: sen(x) = x - x^3/3..  Utilize os valores em radianos(π = 3.14)
'''

pi = 3.14

x = float(input("Digite o valor de X em graus: "))

radiano = x * (pi / 180)

senx = radiano

termo_atual = radiano
sinal = -1
for n in range(2, 16, 2): 
    termo_atual *= (radiano ** 2) / (n * (n + 1))
    senx += sinal * termo_atual
    sinal *= -1

print(f"sen({x}) = {round(senx, 2)}")
