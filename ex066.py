valor = soma = contador = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    soma += valor
    contador += 1
print(f'Foram digitados {contador} valores')
print(f'A soma dos valores digitados foi {soma}')
