reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possivel formar um triangulo com essas retas')
    if reta1 == reta2 == reta3:
        print('Essas retas formam um triangulo equilatero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Essas retas formam um triangulo isosceles')
    else:
        print('Essas retas formam um triangulo escaleno')
else:
    print('Não é possivel formar um triangulo com essas retas!')
