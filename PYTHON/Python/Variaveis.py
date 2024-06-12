#Variaveis primitivas
'''
int -> int()
float -> float()
str -> str()
bool -> bool()
'''

#Variaveis compostas -------------------------------------------

#Tupla
#...

# posição    0         1        2        3
frutas = ("banana", "manga", "maça", "pitaya") # tuple de string

print('Minha tupla', frutas)
print('Tipo da tupla: ', type(frutas))

print('Acessando a posição 3:', frutas[3])
#frutas[0] = 'pitaya' // TUPLA não recebe novos itens.
                        #tupla é imultavel

# 1 a 12 meses - se for menor que 1 e maior que 12
mes = int(input("Insira o mês: "))
if mes<1 or mes>12:
    print("Mês invalido.")
else:
    meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", 
             "agosto", "setembro", "outubro", "novembro", "dezembro", "janeiro")
    print("O mês digitado é:",meses[mes-1])

#percorrendo a tupla
'''
for posicao in range(len(meses)):
    print(meses[posicao])
'''

#percorrendo a tupla de outra forma
'''
for posicao in meses:
    print(posicao)
'''

#contando ocorrencias
controle = 0
for mes in meses:
    if mes == 'janeiro':
        controle += 1

print(controle)

#função
'''
print(meses.count("fevereiro"))
'''
#indice do mes, retorna sempre a primeiro ocorrencia da tupla.
'''
print(meses.index("fevereiro"))
'''
#indice de cada ocorrencia

for indice in range(len(meses)):
    if meses[indice] == "janeiro":
        print(indice)

#Listas
#...

#posicoes    0         1       2         3         4
frutas = ["Banana", "Maça", "Limão", "Pitaya", "Morango"]
print(frutas)
print(len(frutas)) #percorre tamanho da lista
print(frutas[0]) #imprime a posição do indice

for indice in range(len(frutas)): #printa
    print(frutas[indice])

#Insere um item no fim da lista
frutas.append("Melancia")

#remove um item no fim da lista
#frutas.pop()

#remove um item especifico, sempre a primeira ocorrencia
#frutas.remove("Morango")

#insere um item na posição desejada
frutas.insert(3, "Pêra")

#remove um item desejado
frutas.pop(2)

print(frutas)

print("graviola aparece", frutas.count("graviola"))
print("banana aparece", frutas.count("Banana"))
print("Indice da maça:", frutas.index("Maça"))

#procurar um item
tem_pera = False
for indice in range(len(frutas)):
    if (frutas[indice] == "Pêra"):
        #print("Existe Pêra na lista.")
        tem_pera = True

if tem_pera == True:
    print("Tem pera, parabéns filinho.")
else:
    print("Não tem pera filinho.")

#Match
#Repetição que se repete o mesmo caso.
opcao = int(input("insira"))

match opcao:
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print("error")