#18.Escreva um algoritmo que leia o peso e a altura de uma pessoa, calcule e imprima o
#seu IMC. o IMC é dado pela seguinte fórmula: IMC = pesso/altura^2

pesso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = pesso/(altura**2)
rounded = (round(imc,2))
print("O seu indice de massa corporal é:" ,rounded)

if imc<=18.5: 
    print("Seu Indice de massa corporal é de Magreza extrema, consulte um médico.")
elif 24.9<=imc<=18.5:
    print("Seu indice de massa corporal é classificado como ótimo!")
elif 25.0<=imc<=29.9:
    print("Seu indice de massa corporal é de sobrepesso.")
elif 30.0<=imc<=39.9:
    print("Seu indice de massa corporal é de obessidade.")
else:
    print("Seu indice de massa corporal é de Obsessidade extrema, conculte um médico.")