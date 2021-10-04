from unittest import TestCase
from oo.carro.Carro import Carro


class CarroTesteCase(TestCase):

    def test_velocidade_inicial(self):
        carro = Carro()
        self.assertEqual(0, carro.motor.velocidade)

    def test_acelerar(self):
        carro = Carro()
        carro.motor.acelerar()
        self.assertEqual(1, carro.motor.velocidade)

    def test_frear_parado(self):
        carro = Carro()
        carro.motor.frear()
        self.assertEqual(0, carro.motor.velocidade)

    def test_frear_uma_unidade(self):
        carro = Carro()
        carro.motor.acelerar()
        carro.motor.frear()
        self.assertEqual(0, carro.motor.velocidade)

    def test_frear_duas_unidades(self):
        carro = Carro()
        carro.motor.acelerar()
        carro.motor.acelerar()
        carro.motor.frear()
        self.assertEqual(0, carro.motor.velocidade)

    def test_frear_sem_parar(self):
        carro = Carro()
        carro.motor.acelerar()
        carro.motor.acelerar()
        carro.motor.acelerar()
        carro.motor.frear()
        self.assertEqual(1, carro.motor.velocidade)

    def test_direcao_inicial(self):
        carro = Carro()
        self.assertEqual('N', carro.volante.direcao)

    def test_direcao_virar_esquerda(self):
        carro = Carro()
        carro.girar_a_esquerda()
        self.assertEqual('O', carro.volante.direcao)

    def test_direcao_virar_direita(self):
        carro = Carro()
        carro.girar_a_direita()
        self.assertEqual('L', carro.volante.direcao)
