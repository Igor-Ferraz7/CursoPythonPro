def resposta_inteligente(pergunta: str):
    lista = ["NÃO", "NAO", "NEGATIVO", "N", "NO", "NEGATIVE"]
    lista2 = ["SIM", "S", 'POSITIVO', 'COM CERTEZA', "CLARO", 'SI', 'YES', "YEP"]
    while True:
        rsp = input(pergunta).upper().split()
        if rsp == []:
            print('Erro. Valor inválido, digite novamente.')
            continue
        else:
            for c in rsp:
                if c in lista:
                    return 'N'
                elif c in lista2:
                    return 'S'
                else:
                    print('Erro. Valor inválido, digite novamente.')
                    continue


def respostaINT_inteligente(pergunta: str):
    while True:
        try:
            rsp = float(input(pergunta))
            return rsp
        except:
            print('Erro. Valor inválido, digite novamente.')
            continue
# if __name__ == "__main__":
#     a = respostaINT_inteligente("Digite a quantidade que deseja depositar: ")
#     print(a)
