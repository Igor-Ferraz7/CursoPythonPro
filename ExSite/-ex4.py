# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
class Retangulo:
    def __init__(self, ladoA=0, ladoB=0):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valores(self):
        self.ladoA = int(input('Novo ladoA: '))
        self.ladoB = int(input('Novo ladoB: '))

    def retornar_valores(self):
        print(f'LadoA: {self.ladoA}\nLadoB: {self.ladoB}')

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        calculo = (self.ladoA * 2) + (self.ladoB * 2)
        return calculo


if __name__ == "__main__":
    la = int(input('Digite o ladoA: '))
    lb = int(input('Digite o ladoB: '))
    Cal = Retangulo(ladoA=la, ladoB=lb)
    print(f'O número de pisos de 1cm para preencher toda sua área é de {Cal.calcular_area()}\n'
          f'A quantidade de rodapes serão {Cal.calcular_perimetro()}')