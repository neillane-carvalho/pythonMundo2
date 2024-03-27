cont = soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: '))
print('Voce digitou {} valores e a soma entre eles foi {}'.format(cont, soma))
