'''
20. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias

'''

area_para_pintar = float(input("Informe a área para pintura: "))

quantidadetinta = round(area_para_pintar/6, 1)

latasdezoito = round(quantidadetinta/18)

galoestresseis = round(quantidadetinta//3.6)

sobralatas = round(quantidadetinta%18)

sobragaloes = round(quantidadetinta%3.6)

somasobras = round(quantidadetinta//sobralatas+sobragaloes)
dez = somasobras + somasobras*0.10

valordezoito = round(latasdezoito*80)
print(f"Para pintar a área com latas, você deve usar {latasdezoito} latas, no valor de {valordezoito} reais.")

valorgaloes = round(galoestresseis*25)
print(f"Para pintar a área com galões, você deve usar {galoestresseis} galões, no valor de {valorgaloes} reais.")

#valormetades = round(dez*18*3.6)
print(f"Para pintar a área com sobras de latas e galões, você deve usar {dez} galões, no valor de {valormetades} reais.")
#print(f"Se ultilizar a sobra das latas e galõ")
