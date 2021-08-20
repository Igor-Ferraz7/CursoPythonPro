class Bola:
    color = str(input('Qual a primeira cor? '))
    cir = str(input('Qual o tamanho da circunferência? '))
    mat = str(input('Qual o material? '))
    def __init__(self, cor=color, circ=cir, material=mat):
        self.cor = cor
        self.circ = circ
        self.material = material


    def troca_cor(self):
        co = str(input('Qual cor? '))
        self.cor = co


    def mostra_cor(self):
        print(self.cor)



if __name__ == "__main__":
    Ball = Bola()
    Ball.troca_cor()
    Ball.mostra_cor()