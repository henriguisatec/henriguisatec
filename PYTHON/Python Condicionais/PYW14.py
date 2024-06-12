'''
14. Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o
semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
(media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).
'''

nome = str(input("Insira o nome do aluno(a): "))
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insir a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
media = nota1 + nota2 + nota3/3

if media >=7:
    print(("O aluno {} está aprovado.").format(nome))
elif 6.9 >= media and media >= 5.1:
    print(("O aluno(a) {} está de recuperação.").format(nome))
else:
    print(("O aluno(a) {} está reprovado.").format(nome))