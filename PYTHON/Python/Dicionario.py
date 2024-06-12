#Dicionario

maca = {
    'nome': 'Maçã',
    'cor': 'Vermelha'
}

macaverde = {
    'nome': 'Maçã',
    'cor': 'Verde'
}


maca['preço'] = 1.99

print(maca['nome'], maca['cor'], 'valor: ',maca['preço'])

del maca['cor']
print(maca)

lista = []
lista.append(maca)
print(lista)

lista = []
lista.append(macaverde)
print(lista)