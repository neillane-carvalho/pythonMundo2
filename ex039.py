from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today() - nascimento
if idade < 18:
    print('Você ainda não tem idade suficiente para se alistar')
    print('Faltam {} anos para o alistamento'.format(18 - idade))
elif idade >= 18 and idade <= 45:
    print('Você está na hora de se alistar')
else:
    print('Você perdeu a hora de se alistar')
    print('Seu alistamento deveria ser feito há {} anos'.format(idade - 45))
