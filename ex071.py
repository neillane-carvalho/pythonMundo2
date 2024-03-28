print('\033[1;31m=\033[m' * 30)
print('\033[1;31m{:^30}\033[m'.format(' BANCO CEV '))
print('\033[1;31m=\033[m' * 30)
valor = int(input('Que valor deseja sacar? R$'))
total = valor
cedula = 50
totcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedulas = 0
        if total == 0:
            break
print('\033[1;31m=\033[m' * 30)
print('\033[1;31m{:^30}\033[m'.format('VOLTE SEMPRE'))
