classificados = ['Ana', 'Carlos', 'Pedro']
print(f'Lista original: {classificados}')

nome_incorreto = input('Digite o nome incorreto: ')

if nome_incorreto in classificados:
    nome_correto = input('Digite o nome correto: ')
    posicao = classificados.index(nome_incorreto)
    classificados.insert(posicao, nome_correto)
    classificados.remove(nome_incorreto)
    print(f'O nome {nome_incorreto} foi substituído por {nome_correto}.')
    print(f'Lista atualizada: {classificados}')
else:
    print('Nome não encontrado.')
