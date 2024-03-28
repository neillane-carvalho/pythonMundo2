total = totalThousand = lowest = cont = 0
cheap = ' '
while True:
    nameProduct = input('What is your product name? ')
    price = float(input('Enter your product price: '))
    cont += 1
    total += price
    if price > 1000:
        totalThousand += 1
    if cont == 1:
        lowest = price
        cheap = nameProduct
    else:
        if price < lowest:
            lowest = price
            cheap = nameProduct
    response = ' '
    while response not in 'YN':
        response = str(input('Do you want to continue? Y/N: ')).strip().upper()[0]
    if response == 'N':
        break
print('{:-^30}'.format(' END OF PROGRAM '))
print(f'Total price: {total:.2f}')
print(F'There is {totalThousand} products that costs more than $1000.')
print(f'The cheapest product was {cheap} with ${lowest:.2f}')
