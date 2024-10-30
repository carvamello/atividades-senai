print('Olá seja bem vindo!')
val_inicial = int(input('informe o valor inicial\n'))
val_final = int(input('Informe o valor final:\n'))
incremento = int(input('informe o incremento:\n'))
for i in range(val_inicial,val_final,-incremento):
    print(i)
