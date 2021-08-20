class Conta():
    def __init__(self, contas=None):
        self.VL = ['Digite o valor da Varição do Comprimento: ', 0]
        self.Lo = ['Digite o valor de Lo(comprimento inicial): ', 1]
        self.ALF = ['Digite o valor do Coeficiente de Dilatação linear: ', 2]
        self.VT = ['Digite o valor da Variação da Temperatura: ', 3]
        self.Lf = ['Digite o valor de Lf(comprimento final): ', 4]
        self.contaVL = self.Lo[1] * self.ALF[1] * self.VT[1]
        self.contaLo = self.VL[1] * self.ALF[1] * self.VT[1]
        self.contaALF = self.Lo[1] * self.VL[1] * self.VT[1]
        self.contaVT = self.Lo[1] * self.ALF[1] * self.VL[1]

    def dilatacao_linear(self):
        print("""[0] Varição do comprimento
[1] Comprimento Inicial
[3] Variação da Temperatura
[2] Coeficiente de Dilatação linear
[4] Comprimento Final""")
        dc = int(input('Digite o valor que queira descobrir: '))
        lista = []
        p = Conta().__dict__
        print(p)
        for k, v in p.copy().items():
            print(v[1])
            if v[1] == dc:
                p.pop(k)
                print('test')
        for k, v in p.items():
            lista.append(int(input(v[0])))
        if dc == 0:
            conta = Conta().dilatacao_linear()
            conta1 = conta.VL
            print(conta1)

        print(lista)
Conta().dilatacao_linear()
