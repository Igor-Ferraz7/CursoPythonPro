from n import rsp_qi
"""
 -> Crie uma classe para implementar uma conta corrente.
 A classe deve possuir os seguintes:

 --> Atributos: número da conta, nome do correntista e saldo.
 --> Métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
 com valor default zero e os demais atributos são obrigatórios.
 """
class Conta_corrente:
    def __init__(self, ndcont: int, ndcor: str, saldo: int = 0):
        self.numero_da_conta = ndcont
        self.nome_do_correntista = ndcor
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_do_correntista = novo_nome

    def deposito(self):
        rsp = rsp_qi.resposta_inteligente(f'Olá {self.nome_do_correntista}! Atualmente possui R${self.saldo:.2f} depositado. Deseja depositar mais? ')
        if rsp == 'S':
            self.saldo += rsp_qi.respostaINT_inteligente('Digite a quantidade que deseja depositar: R$')

    def saque(self):
        ndo = rsp_qi.respostaINT_inteligente('Digite a quantia que deseja sacar: R$')
        if ndo > self.saldo:
            while ndo > self.saldo:
                ndo = rsp_qi.respostaINT_inteligente(f'Erro. O máximo que pode saquar é R${self.saldo:.2f}. Digite q quantia: ')
            self.saldo -= ndo
            print(f'Saque realizado com sucesso! Agora você possui R${self.saldo:.2f}')
        else:
            self.saldo -= ndo
            print(f'Saque realizado com sucesso! Agora você tem R${self.saldo:.2f} de saldo.')


if __name__ == '__main__':
    asd = Conta_corrente(ndcont=900123, ndcor='Igor Ferraz')
    asd.alterar_nome('Igor Sousa')
    asd.deposito()
    asd.saque()
