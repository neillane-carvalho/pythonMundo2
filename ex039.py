from datetime import date
atual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = atual - nascimento
if idade < 18:
    print('Você ainda não tem idade suficiente para se alistar')
    print('Faltam {} anos para o alistamento'.format(18 - idade))
elif 18 <= idade <= 45:
    print('Você está na hora de se alistar')
else:
    print('Você perdeu a hora de se alistar')
    print('Seu alistamento deveria ser feito há {} anos'.format(idade - 45))
