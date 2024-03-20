valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos voce vai pagar? '))
prestacao = valor_casa / anos
if prestacao <= (salario * 30 / 100):
    print('Seu emprestimo foi aprovado!')
    print('O valor da sua parcela sera R${:.2f}'.format(prestacao))
else:
    print('Seu emprestimo foi negado!')
    print('O valor da sua parcela (R${:.2f}) é maior que 30% do seu salario!'.format(prestacao))
