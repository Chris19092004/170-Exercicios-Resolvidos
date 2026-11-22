'''Exercício 08:
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.''' 

valor_hora = float(input("Quantos R$ você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalhou nesse mês? "))
valor_final = valor_hora * horas_mes

print (f"\nNesse mês, você recebeu R${valor_final:.2f}")
