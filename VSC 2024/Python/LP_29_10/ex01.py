# Função
from os import lstat


def fun_sorted(arg):
    n = len(arg)  # Recebe o tamanho da lista
    for i in range(n):
        for j in range(0, n-i-1):  # Loop pra comparar elementos
            if arg[j] > arg[j + 1]:
                arg[j], arg[j + 1] = arg[j + 1], arg[j]
    return arg
def add_lista(arg):
    num = int()
    while num != 999:
        num = int(input('Informe os numeros:\n'))
        arg.append(num)

# Código 
lista = []
add_lista(lista)
fun_sorted(lista)
print(lista)