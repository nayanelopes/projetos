print("Qual sua nota na primeira unidade?", end='', flush=True)
nota1 = float(input())
print("Qual sua nota na segunda unidade?", end='', flush=True)
nota2 = float(input())
print("Qual sua nota na terceira unidade?", end='', flush=True)
nota3 = float(input())
print("Qual sua nota na quarta unidade?", end='', flush=True)
nota4 = float(input())
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print("Preciso estudar mais")
else:
    print("Eu fui um bom aluno")
