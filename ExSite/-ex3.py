class Quadrado:
    tam = int(input('Tamanho do lado: '))

    def __init__(self, tamanho_do_lado=tam):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self):
        mud = int(input('Insire o novo valor do lado: '))
        self.tamanho_do_lado = mud

    def retornar_valor_do_lado(self):
        print(self.tamanho_do_lado)

    def calcular_area(self):
        ld = self.tamanho_do_lado
        calculo = ld * ld
        print(f'Área: {calculo}')


if __name__ == "__main__":
    Quadrado = Quadrado()
    Quadrado.retornar_valor_do_lado()
    Quadrado.mudar_valor_do_lado()
    Quadrado.retornar_valor_do_lado()
    Quadrado.calcular_area()
