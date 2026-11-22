'''Exercício 04:
Faça um programa que peça as 4 notas bimestrais e mostre a média.'''

notas = []
for i in range (1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

print (f"\nA média do aluno é {sum(notas)/4}")
