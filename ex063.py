print('-=-' * 20)
print('\033[1;31mSEQUENCIA DE FIBONACCI\033[m')
print('-=-' * 20)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
