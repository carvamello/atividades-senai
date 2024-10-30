valor_inicial = int(input('Informe o valor inicial\n'))
valor_final = int(input('Informe o valor final\n'))
incremento = int(input('informe o valor de incremento\n'))
print('')
for i in range(valor_inicial,valor_final,incremento):
    print(f'\033[34m{i}\033[m',end=' ')
    
if incremento + 1:
    print('\n\033[33mCrescente\033[m\n')
else:
    print('\n\033[33mDecrescente\033[m\n')