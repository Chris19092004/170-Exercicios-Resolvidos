'''Exercício 09:
Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''

f = int(input("Digite a temperatura em farenheit: "))
c = 5 * ((f-32)/9)

print(f"\n{f}ºF equivalem a {c:.1f}ºC")
