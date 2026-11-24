'''Exercício 11:
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

    O produto do dobro do primeiro com metade do segundo .
    A soma do triplo do primeiro com o terceiro.
    O terceiro elevado ao cubo.'''

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = float(input("Digite um número real: "))

print (f"\n\nO produto do dobro do primeiro com metade do segundo: {n1*2} x {n2/2} = {(n1*2)*(n2/2)}")
print (f"\nA soma do triplo do primeiro com o terceiro: {n1*3} + {n3} = {(n1*3)+n3}")
print (f"\nO terceiro elevado ao cubo = {n3}³ = {n3**3:.2f}")
