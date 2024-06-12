#8. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele
#obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = str(input("Insira o nome do aluno: "))
nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: " ))
media = nota1 + nota2 + nota3/3
rounder = round(media, 1)
print(("A media de {} é {}").format(nome,rounder))