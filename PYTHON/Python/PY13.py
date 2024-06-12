#13. Faça um algoritmo que receba um valor que foi depositado e exiba o valor com
#endimento após um mês.
#Considere fixo o juro da poupança em 0,70% a. m.

depo = float(input("Insira o valor que foi depositado: "))
juro = depo*0.007
rend = depo + juro
rounded = round(rend, 6)
print(("O rendimento após um mês foi de: {}").format(rounded))