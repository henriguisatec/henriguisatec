#12. Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$)
#de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
#dólar e também a quantidade de dólares disponíveis com o usuário.

dolarbill = float(input("Insira o valor em dolar: "))
cotag = float(input("Insira a cotação do dolar atual: "))
real = dolarbill/cotag
rounded = round(real,2)
print(("O valor inserido de {} U$ convertido pra real é {}").format(dolarbill,rounded))