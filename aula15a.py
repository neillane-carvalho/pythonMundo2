#comando break
valor = soma = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    soma += valor
print(f'A soma dos valores digitados foi {soma}')