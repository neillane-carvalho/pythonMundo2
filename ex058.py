from random import randint

computer = randint(0, 10)
print('\033[1;33mVou pensar em um numero entre 0 e 10. Tente advinhar...\033[m')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('Mais!')
        elif jogador > computer:
            print('Menos!')
print('Acertou com {} tentativas'.format(palpites))
