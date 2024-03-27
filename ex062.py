print('\033[1;32m GERADOR DE PA\033[m')
print('-=-' * 15)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    print('-=-' * 15)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM DA PA')
