from unittest import TestCase
from ExSite.classe_carro_resolucao import Motor


class Test_Carro(TestCase):
    def teste_de_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_do_acelerar(self):
     motor = Motor()
     motor.acelerar()
     self.assertEqual(1, motor.velocidade)