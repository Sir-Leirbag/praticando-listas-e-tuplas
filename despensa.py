despensa = ['açucar', 'macarrão', 'arroz', 'feião']

item = input('Digite o item que você quer verificar:')

if item in despensa:
    print(f'Já possui o item {item} na despensa.')
else:
    print(f'O item {item} precisa ser comprado')
