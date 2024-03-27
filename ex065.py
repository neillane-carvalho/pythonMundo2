resposta = 'Ss'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('A quantidade de valores digitados foi {} e sua media foi {:.2f}'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
print('Obrigado por utilizar o nosso programa!')