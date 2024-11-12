import os
import time as t
os.system('cls')
t.sleep(0.6)
print(f'''
-----------------------------------------------------
---------- Seja bem vindo(a) a forja ----------------
-----------------------------------------------------
''')

def verificar(arg):
    itens_formatados = []
    for i in range(0,len(arg),2):
        item = arg[i][0]
        preco = arg[i + 1][0]
        itens_formatados.append(f'{item} --> R${preco:.2f} Reais')
        print(f'{item} R${preco:.2f}')



itens = [['Machado'],[10.00],['Espada'],[20.00]]
i = 0
while i < 1:
    i += 1
    menu = input('1. Comprar\n2. Vender\n3. Forjar\n ')
    print('\n')
    if menu in '1':
        verificar(itens)
    print('\n')