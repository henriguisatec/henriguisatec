#9. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua
#média ponderada (as notas têm pesos respectivos de 1, 2 e 3).

nome = str(input("Insira o nome do aluno: "))
nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: " ))
media = nota1*1 + nota2*2 + nota3*3/1+2+3
rounder = round(media, 1)
print(("A media de {} é {}").format(nome,rounder))