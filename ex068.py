from random import randint

vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}, total de {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print(f"Voce venceu!")
            vitorias += 1
    elif tipo == 'I':
        if total % 2 == 1:
            print(f"Voce venceu!")
            vitorias += 1
        else:
            print(f"Voce perdeu!")
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {vitorias} vezes')
