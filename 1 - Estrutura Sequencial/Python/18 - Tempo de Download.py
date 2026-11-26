"""Exercício 18:
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos)."""

arquivo = float(
    input("Digite o tamanho do arquivo para download (em MB): ")
)  # MegaBytes
internet = float(
    input("Digite a velocidade do link de internet (em Mbps): ")
)  # Megabits

# 1 Byte -> 8 bits

# Fórmula: tempo (em segundos) = (tamanho do arquivo x 8) / velocidade de internet
# Depois, divide por 60 para obter o tempo em minutos

tempo_download = ((arquivo * 8) / internet) / 60

print(
    f"\nEsse arquivo levará aproximadamente {round(tempo_download, 1)} minutos para ser concluído."
)

# Algumas saídas testadas

# 500 MB e 5 mbps = 13.3 minutos -> equivalente a 13 minutos e 18 segundos
# 1 MB e 1 mbps = 0.1 minutos -> equivalente a 6 segundos
# 2000 MB e 10 mbps = 26.7 minutos -> equivalente a 26 minutos e 42 segundos
# 1500 MB e 1 mbps = 200 minutos -> equivalente a 3 horas e 20 minutos
