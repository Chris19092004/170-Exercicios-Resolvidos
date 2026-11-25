'''Exercício 16:
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

area = float(input("Digite o tamanho (em m²) da área a ser pintada: "))
litro_metro_quadrado = 3
quantidade_latas = 1
litro_lata = 18
preco_lata = 80

while (litro_lata*litro_metro_quadrado) < area:
    litro_lata = litro_lata + 18
    quantidade_latas+=1
    preco_lata = preco_lata + 80

print (f"\nVocê precisará comprar {quantidade_latas} latas, e pagará R${preco_lata:.2f}")
