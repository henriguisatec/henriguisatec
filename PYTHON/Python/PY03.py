# 3) Crie um algoritmo para calcular a area de um quadrado, retangulo, triangulo e circulo.

ladquad = float(input("Para calcular a área do quadrado, primeiro, insira o valor de um lado: "))
quad = ladquad * ladquad
print("A aréa do quadrado é: {}".format(quad))

baseret = float(input("Para calcular a área do retangulo, insira o valor de um dos lados menores: "))
ladret = float(input("Agora, insira o valor do lado maior: "))
ret = baseret * ladret
print("A área do retangulo é: {}".format(ret))

basetri = float(input("Para calcular a área do triangulo, insira o valor da base: "))
alturatri = float(input("Agora, insira a altura do triangulo: "))
triang = basetri * alturatri / 2
print("A aréa do triangulo é: {}".format(triang))