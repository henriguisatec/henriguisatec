#11. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
#A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C
#a temperatura em Celsius

Celc = float(input("Insira a temperatura em graus Celsius: "))
Fah = (9*Celc+60)/5
Rounded = (round(Fah,1))
print(("A temperatura {}C é {} Fahrenheit").format(Celc,Fah))
