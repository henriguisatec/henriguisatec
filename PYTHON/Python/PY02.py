# 2) Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e divisão dos números lidos.
num1 = float(input("Insira um número: "))
num2 = float(input("Insira um segundo número: "))
sum = num1 + num2
print("A soma entre ",num1, "e" ,num2, "é: ",sum)
sub = num1 - num2
print("A subtração entre ",num1, "e" ,num2, "é: ",sub)
multiplication = num1 * num2
print("A multiplicação entre  {} e {} é: {}".format(num1, num2, multiplication))
division = num1 / num2
print("A divisão entre {} e {} é: {}".format(num1, num2, division))