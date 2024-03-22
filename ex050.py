soma = 0
count = 0
for c in range(1, 7):
    numbers = int(input(f'Digite o {c} valor: '))
    if numbers % 2 == 0:
        soma += numbers
        count += 1
print(f'Voce digitou {count} valores pares e a soma entre eles foi {soma}')
