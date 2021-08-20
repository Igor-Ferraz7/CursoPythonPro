def reverse_words(s):
    """
    Inverte uma frase
    Ex:
        >>>reverse_words('the sky is blue')
        blue is sky the
    :param s:
    :return:
    """
    lista = s.split() #lista = ['ola', 'mundo']
    for c in range(1, len(lista)+1): #c = 1, c = 2
        print(lista[-c], end=' ')


reverse_words('the sky is blue')
