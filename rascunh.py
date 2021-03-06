"""
ATRIBUTOS DE CLASSE
- DEFINE UM VALOR PADRÃO (ESTADO) PARA TODOS OS ELEMENTOS DE UMA CLASSE
- ALTERA O VALOR PADRÃO EM CADA OBJETO: EXEMPLO: TODOS MORAM EM ALAGOAS MAS MORAM EM CIDADES DIFERENTES
- ALTERA O VALOR PADRÃO DA CLASSE. EXEMPLO: SÃO PAULO
"""


class Pessoa:  # Segundo a pep8 classes começa com letra maiuscula
    estado_cidade = 'Alagoas'  # atributo default / classe

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):  # metodo
        return f'Ola {id(self)}'


if __name__ == "__main__":
    rayanne = Pessoa(nome='Rayanne')
    paula = Pessoa(rayanne, nome='Paula')
    ana = Pessoa(rayanne, paula, nome='Ana')
    sergio = Pessoa(rayanne, paula, ana, nome='Sergio')
    paulo = Pessoa(rayanne, paula, ana, sergio, nome='Paulo')
    gustavo = Pessoa(rayanne, paula, ana, sergio, paulo, nome='Gustavo')
    rafael = Pessoa(rayanne, paula, ana, sergio, paulo, gustavo, nome='Rafael')  # gustavo filho do Rafael
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())  # objeto.metodo() ==> ja passa o objeto p implicitamente
    print(rafael.nome)
    print(rafael.idade)
    print('Filhos: ')
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Gomes'  # atributo dinamico
    Pessoa.estado_cidade = 'São Paulo'  # modifica para todos os objetos um novo valor default
    rayanne.estado_cidade = 'Arapiraca'
    paula.estado_cidade = 'Rio Largo'
    ana.estado_cidade = 'Maceio'
    sergio.estado_cidade = 'Anadia'
    paulo.estado_cidade = 'Marechal Deodoro'
    gustavo.estado_cidade = 'Maribondo'
    rafael.estado_cidade = 'São Miguel dos Campos'
    print(rafael.sobrenome)
    print(rafael.__dict__)  # informa todos os atributos de instancia ligados ao objeto nome(rafael)
    print(gustavo.__dict__)
    print('Estado: ')
    print(Pessoa.estado_cidade)  # para a classe
    print('Cidades: ')
    print(rayanne.estado_cidade, paula.estado_cidade, ana.estado_cidade, sergio.estado_cidade, paulo.estado_cidade,
          gustavo.estado_cidade, rafael.estado_cidade)

