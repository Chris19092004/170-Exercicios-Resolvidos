'''Exercício 16:
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

from math import ceil

area = float(input("Digite o tamanho (em m²) da área a ser pintada: "))

litro_metro = 1 / 3
litros_necessarios = area * litro_metro
litros_lata = 18
preco_lata = 80

quantidade_latas = ceil(litros_necessarios / litros_lata)
preco_total = quantidade_latas * preco_lata

print (f"\nVocê precisará comprar {quantidade_latas} latas, e pagará R${preco_total:.2f}")
