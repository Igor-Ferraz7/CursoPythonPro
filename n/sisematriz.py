def menu(nome, simbo):
    simb = f'{simbo}'*20
    print(f'{simb}\n{nome:^40}\n{simb}')


def tabuada(num, quant):
    int(num)
    for c in range(0, quant+1):
        print(f'{num}x{c}={num*c}')


def matrizestetic(lista):
    menu('Estética da Matriz', '==')
    lista1 = []
    n = 0
    for c in lista.values():
        n += 1
        lista1.append(c)
        if n == 1:
            print(f'{" "*15}', end='')
        print(f'[{c}]', end=' ')
        if n == 3:
            if c == lista1[2]:
                print(f'\n{" "*15}', end='')
        if n == 6:
            if c == lista1[5]:
                print(f'\n{" " * 15}', end='')
    print('\n', '=='*20)


def matriz3x3():
    ListOfMatriz = {}
    for c in range(1, 10):
        if c <= 3:
            if c == 1:
                menu('Primeira linha', '-=')
            vm = int(input(f'a1x{c}: '))
            ListOfMatriz[f'a1x{c}'] = vm
        if 3 < c <= 6:
            if c == 4:
                menu('Segunda linha', '-=')
            c -= 3
            vm = int(input(f'a2x{c}: '))
            ListOfMatriz[f'a2x{c}'] = vm
            c += 3
        if c > 6:
            if c == 7:
                menu('Terceira linha', '-=')
            c -= 6
            vm = int(input(f'a3x{c}: '))
            ListOfMatriz[f'a3x{c}'] = vm
    matrizestetic(ListOfMatriz)
    def detmatriz3x3():
        cp1 = ListOfMatriz['a1x1'] * ListOfMatriz['a2x2'] * ListOfMatriz['a3x3']
        cp2 = ListOfMatriz['a1x2'] * ListOfMatriz['a2x3'] * ListOfMatriz['a3x1']
        cp3 = ListOfMatriz['a1x3'] * ListOfMatriz['a2x1'] * ListOfMatriz['a3x2']
        ctotp = cp1 + cp2 + cp3
        cn1 = (ListOfMatriz['a1x3']* -1) * (ListOfMatriz['a2x2']* -1) * (ListOfMatriz['a3x1']* -1)
        cn2 = (ListOfMatriz['a1x1']* -1) * (ListOfMatriz['a2x3']* -1) * (ListOfMatriz['a3x2']* -1)
        cn3 = (ListOfMatriz['a1x2']* -1) * (ListOfMatriz['a2x1']* -1) * (ListOfMatriz['a3x3']* -1)
        ctotn = cn1 + cn2 + cn3
        ctot = ctotp + ctotn
        print(f'A determinante é {ctot}')
    detmatriz3x3()


# def matriz4x4():

