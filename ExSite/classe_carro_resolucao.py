"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

 A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

       N
    O     L
       S
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direct:
    lista = ["Norte", "Leste", "Sul", "Oeste"]

    def __init__(self):
        self.valor = self.lista[0]

    def girar_a_direita(self):
        n = self.lista.index(self.valor)
        n += 1
        if n > 3:
            n = 0
        self.valor = self.lista[n]

    def girar_a_esquerda(self):
        n = self.lista.index(self.valor)
        n -= 1
        if n == 0:
            n = 3
        self.valor = self.lista[n]


class carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_a_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar

    def frear(self):
        return self.motor.frear

    def calcular_a_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda


if __name__ == "__main__":
    motor = Motor()
    direcao = Direct()
    Carro = carro(motor, direcao)
    # print(Carro.calcular_a_velocidade())
    Carro.calcular_a_velocidade()
    print(Carro.calcular_a_direcao())
