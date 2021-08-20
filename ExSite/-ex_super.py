"""
Classe ObjetoGrafico subclasse de object, com atributos:
-> cor de preenximento => inteiro
-> preenxida => bool
-> cor de contorno => inteiro

Classes que serão subclasses de ObketoGrafico q tenham metodos de area e perimetro:
-> Retangulo --. Atributos: base e altura
-> Circulo --> Atributos: raio
--> Triangulo --> Atributos: base e altura
"""


class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento:int, preenxida:False, cor_de_contorno:int):
        self.cor_de_preenximento = cor_de_preenximento
        self.preenxida = preenxida
        self.cor_de_contorno = cor_de_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, base, altura):
        super(Retangulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura


# if __name__ == '__main__':
#     ObGr = ObjetoGrafico(cor_de_preenximento=2, preenxida=True, cor_de_contorno=7)
#     Rt = Retangulo(cor_de_contorno=2, preenxida=4, cor_de_preenximento=True, base=12, altura=23)
#     print(ObGr.cor_de_preenximento)