from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:  # pedra
        print('EMPATE')
        print('-=' * 11)
    if jogador == 1:
        print('JOGADOR VENCEU')
        print('-=' * 11)
    if computador == 2:
        print('COMPUTADOR VENCEU')
        print('-=' * 11)
elif computador == 1:  # papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
        print('-=' * 11)
    if jogador == 1:
        print('EMPATE')
        print('-=' * 11)
    if computador == 2:
        print('JOGADOR VENCEU')
        print('-=' * 11)
elif computador == 2:  # tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
        print('-=' * 11)
    if computador == 1:
        print('COMPUTADOR VENCEU')
        print('-=' * 11)
    if computador == 2:
        print('EMPATE')
        print('-=' * 11)
else:
    print('JOGADA INVÁLIDA')
    print('-=' * 11)
