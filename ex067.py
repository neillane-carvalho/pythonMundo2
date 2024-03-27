# taboada de varios numeros
while True:
    núm = int(input('Quer ver a tabuada de qual numero? '))
    if núm < 0:
        break
    print(F'\033[1;31m TABOADA DE {núm} \033[m')
    for c in range(1, 11):
        print(f' | {núm} x {c} = {núm * c}')
    print('\033[1;32mFIM\033[m')
print('\033[1;31mPROGRAMA FINALIZADO!\033[m')
