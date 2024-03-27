numero = int(input('Digite um numero para calcular seu fatorial: '))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
