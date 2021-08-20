def contar_letras(s: str):
    dc = {}
    for c in s:
        dc[c] = s.count(c)
    return dc


print(contar_letras('bananaoufits'))

