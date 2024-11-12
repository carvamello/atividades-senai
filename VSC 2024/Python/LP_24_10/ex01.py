
from tracemalloc import stop


while True:
    a = int(input('Informe o valor de A: '))
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de C: '))
    print(f'Valor de A {a}\nValor de B {b}\nValor de C {c}')

    alt = input('Deseja cotinuar? ')
    if alt == 'n':
        break