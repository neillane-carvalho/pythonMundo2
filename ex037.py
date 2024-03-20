numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção invalida')
