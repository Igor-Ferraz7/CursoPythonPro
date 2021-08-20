"""
----> Classe Pessoa: Crie uma classe que modele uma pessoa:
 --> Atributos: nome, idade, peso e altura
 --> Métodos: Envelhercer, engordar, emagrecer, crescer.
 --> Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
  ela deve crescer 0,5 cm.
 """
class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):
        self.idade += 1

    def Engordar(self):
        self.peso += 1.2

    def Emagrecer(self):
        self.peso -= 0.4

    def Crescer(self):
        if self.idade < 21:
            self.altura += (0.5 * self.idade)
        else:
            self.altura += (0.2 * (self.idade - 21) + 0.5 * 21)


if __name__ == "__main__":
    PP = Pessoa("Igor", 22, 40, 1.74)
    PP.Crescer()
    for k, v in PP.__dict__.items(): #--> anteriormente deu um erro "ValueError: too many values to unpack (expected 2)",
        print(f"{k}: {v}")                     # pois esqueci de colocar o ".items()".
