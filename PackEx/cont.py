def contar_caracteres(st):
    """Conta carcteres

        Ex:
    >>>contar_caracteres('Igor')
    {'i': 1, 'g': 1, 'o': 1, 'r': 1,}
    """
    contagem = n1 = 1
    caracteres_ordenados = sorted(st.lower())
    caracteres_anterior = caracteres_ordenados[0]
    resultado = {}
    for c in caracteres_ordenados[1:]:
        if c == caracteres_anterior:
            contagem += 1
        else:
            # print(f'{caracteres_anterior}: {contagem} vez(es)')
            resultado[caracteres_anterior] = contagem
            caracteres_anterior = c
            contagem = 1
    resultado[caracteres_anterior] = contagem
    return resultado


def fizz_buzz(n: int):
    """
    >>>fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz
    :param n: limite
    :return:
    """
    for c in range(1, n+1):
        if c % 3 == 0 and c % 2 == 0:
            print("fizzbuzz")
        elif c % 2 == 0:
            print('fizz')
        elif c % 3 == 0:
            print('buzz')
        else:
            print(c)


if __name__ == "__main__":
    fizz_buzz(6)