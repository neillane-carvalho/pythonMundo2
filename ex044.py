preco_normal = float(input('Digite o valor do produto: R$'))
print('{:=^30}'.format(''))
print('''FORMAS DE PAGAMENTO
[1] A vista dinheiro 
[2] A vista no cartão
[3] Em até duas 2x no cartão
[4] 3x ou mais no cartão''')
print('{:=^30}'.format(''))
opcao = int(input('Escolha a forma de pagamento: '))
if opcao == 1:
    total = preco_normal - (preco_normal * 0.10)
    print('O valor do produto com 10% de desconto é R${:.2f}'.format(total))
elif opcao == 2:
    total = preco_normal - (preco_normal * 0.05)
    print('O valor do produto com 5% de desconto é R${:.2f}'.format(total))
elif opcao == 3:
    parcela = preco_normal / 2
    print('O valor do produto é R${:.2f} e sua parcela é de R${:.2f}'.format(preco_normal, parcela))
elif opcao == 4:
    total = preco_normal + (preco_normal * 0.20)
    parcela = int(input('Digite em quantas parcelas: '))
    parcela = total / parcela
    print('O valor do produto com 20% de juros fica R${:.2f} e sua parcela é de R${:.2f}'.format(total, parcela))
