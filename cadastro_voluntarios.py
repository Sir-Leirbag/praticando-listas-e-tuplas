lista_de_voluntarios = []

while True:
    nome = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break
    lista_de_voluntarios.append(nome)

print('Voluntários registrados:', lista_de_voluntarios)
