# Aula de Lógica de Programação
#                       Dia 24 de Outubro de 2024


    # Bibliotecas
import os
from time import sleep

    # Variáveis
lista = []
cont = 0

def valores(valor1, valor2):
    print(f'''\n
    primeiro valor \033[32m{valor1}\033[m
    segundo valor \033[32m{valor2}\033[m
    valor da soma: \033[36m{valor1 + valor2}\033[m
    ''')
    # Início
print('Olá Mundo!')
valor_inicial = int(input('informe um valor:\n'))   # Recebe o valor inicial
valor_final = int(input('informe o segundo valor:\n'))  # Recebe o valor Final
#incremento = int(input('informe o valor de incremento\n'))  # Rebece o parâmetro de contagem
valores(valor_inicial,valor_final)
#print('contagem:\n')
'''for i in range(valor_inicial,valor_final,incremento):
    lista.append(i)     # Insere o index na lista
    print(f'\033[32m{i}\033[m')    # Imprime o valor do index
    sleep(0.3)    # Sistema para por 1 segundo
    os.system('cls')    # Sistema limpa o console de comando
print(f'\033[33m{lista}\033[m')'''


