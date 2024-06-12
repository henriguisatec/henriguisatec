texto = "Desenvolver Algoritmos"
tamanho_texto = len(texto)

print(texto)
print(tamanho_texto)

for i in range(tamanho_texto):
    print(type(i))
    print(texto[i], end='')

for caractere in texto:
    print(type(caractere))
    print(caractere)