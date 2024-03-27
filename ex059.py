n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''\033[1;33m    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\033[m''')
    opcao = int(input('Qual a sua opção? '))
    print('Processando...')
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('O produto entre {} e {} vale {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior valor é {}'.format(n2, n1, n2))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('\033[1;Opção invalida\033[')
print('Fim do programa')
