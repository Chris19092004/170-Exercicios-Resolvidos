"""Exercício 17
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias."""

# Esse foi um exercício que me consumiu bastante tempo, e errei.
# Corriji o código com documentação do Python e o Claude, e ao longo
# dele podem-se ver notas de aprendizado para os próximos exercícios/projetos

import math

area = float(input("Digite em m² a área a ser pintada: "))

# LIÇÃO 1: releia o enunciado no final, item por item.
# A folga de 10% valia para as 3 situações, mas eu só a tinha aplicado na 3ª.
# Calculando o valor base uma única vez, aqui no começo, todas as situações
# partem do mesmo número e não há como uma delas ficar diferente das outras.
litro_metro = 1 / 6
folga = 1.10
litros_necessarios = area * litro_metro * folga

litros_lata = 18
preco_lata = 80
litros_galao = 3.6
preco_galao = 25

# Situação 1: apenas latas
quantidade_latas = math.ceil(litros_necessarios / litros_lata)
preco_apenas_latas = quantidade_latas * preco_lata

# Situação 2: apenas galões
quantidade_galoes = math.ceil(litros_necessarios / litros_galao)
preco_apenas_galoes = quantidade_galoes * preco_galao

print(
    f"\nVocê precisará comprar {quantidade_latas} latas, e pagará R${preco_apenas_latas:.2f}"
)
print(
    f"Você precisará comprar {quantidade_galoes} galões, e pagará R${preco_apenas_galoes:.2f}"
)

# Situação 3: latas + galões

# LIÇÃO 2: nome novo para significado novo.
# Eu reaproveitava quantidade_latas e quantidade_galoes aqui. Funcionava, mas
# misturava dois cenários na mesma variável. Antes eu também tinha uma variável
# chamada area_folga que, na verdade, guardava litros. O nome precisa dizer o
# que a variável guarda, senão o próprio autor se confunde depois.
latas_mistura = math.trunc(litros_necessarios / litros_lata)

# LIÇÃO 3: ao subtrair, pergunte "quanto, no total?".
# O erro era subtrair só UMA lata (18 L), mesmo comprando várias. O código dava
# certo quando latas_mistura valia 1, então o bug passou despercebido. Um código
# que funciona em um caso pode estar certo só por coincidência.
litros_restantes = litros_necessarios - (latas_mistura * litros_lata)

galoes_mistura = math.ceil(litros_restantes / litros_galao)

preco_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)

desperdicio = (
    (litros_lata * latas_mistura) + (litros_galao * galoes_mistura)
) - litros_necessarios

print(
    f"Você precisará comprar {latas_mistura} latas e {galoes_mistura} galões, desperdiçando {desperdicio:.1f}L e pagando R${preco_mistura:.2f}"
)
