primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
termo = primeiro + (10 - 1) * razao
for c in range(primeiro, termo + razao, razao):
    print(f'{c}', end='->')
print('ACABOU')