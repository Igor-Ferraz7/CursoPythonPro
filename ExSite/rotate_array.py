def rotate_array(n: int, ek: int):
    """
    >>> rotate_array(7, 3)
    5, 6, 7, 1, 2, 3, 4

    :param n: número de números em ordem crescente em uma lista
    :param ek: número de elementos seguidos que serão pulados "ek" vezes
    :return:
    """
    lista = []
    # lista = range(1, n+1)
    for c in range(1, n+1): #[1, 2, 3, 4, 5, 6, 7]
        lista.append(c)
    if ek+1 in lista[0:ek]:
        transporte = lista[0:ek] #[1, 2, 3, 4]
        del lista[0:ek] #lista = [5, 6, 7]
    else:
        transporte = lista[0:ek+1] #[1, 2, 3, 4]
        del lista[0:ek+1] #lista = [5, 6, 7]
    lista.append(transporte) #lista = [5, 6, 7, [1, 2, 3, 4]]
    print(f"{str(lista).replace('[', '').replace(']', '')}")


rotate_array(7, 3)
