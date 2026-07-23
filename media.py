notas = input('Digite as notas dos alunos separadas por vírgula: ').split(', ')
soma = sum(float(nota) for nota in notas)
media = soma / len(notas)
print(f'Média final da turma: {media:.2f}')
