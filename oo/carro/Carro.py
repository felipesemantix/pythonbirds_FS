from oo.carro.Direcao import Direcao
from oo.carro.Motor import Motor


class Carro:
    """
    Você deve criar uma classe carro que vai possuir dois
    atributos compostos por outras duas classes:

    1) Motor
    2) Direção

    O Motor terá a responsabilidade de controlar a velocidade.
    Ele oferece os seguintes atributos:
    1) Atributo de dado velocidade
    2) Método acelerar, que deverá incrimentar a velocidade de uma unidade
    3) Método frear que você deverá decrementar a velocidade em duas unidades

    A Direcao terá a responsabilidade de controlar a direcao. Ela oferece
    os seguintes atributos:
    1) Valor de direcao com valores possíveis: Norte, Sul, Leste, Oeste.
    2) Método girar_a_direta
    3) Método girar_a_esquerda
      N
    O   L
      S
    """

    def __init__(self):
        self.volante = Direcao()
        self.motor = Motor()

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_esquerda(self):
        self.volante.girar_esquerda()

    def girar_a_direita(self):
        self.volante.girar_direta()


if __name__ == '__main__':
    carro = Carro()
    print("Verificando as condições iniciais dos atributos da Classe: ")
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Testando o Motor: ")
    print()
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Freando o carro...")
    carro.frear()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Freando o carro parado...")
    carro.frear()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Freando o carro...")
    carro.frear()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print("Acelerando o carro uma unidade...")
    carro.acelerar()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Parando o carro...")
    carro.frear()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    carro.frear()
    print("A velocidade atual do carro é: ", carro.motor.velocidade)
    print()
    print("Testando a direção:")
    print("Girando a direção para a direta")
    carro.girar_a_direita()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a direta")
    carro.girar_a_direita()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a direta")
    carro.girar_a_direita()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a direta")
    carro.girar_a_direita()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a esquerda")
    carro.girar_a_esquerda()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a esquerda")
    carro.girar_a_esquerda()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a esquerda")
    carro.girar_a_esquerda()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("Girando a direção para a esquerda")
    carro.girar_a_esquerda()
    print("A direção atual do carro é : ", carro.volante.direcao)
    print()
    print("Verificando as condições atuais dos atributos da Classe: ")
    print("A direção atual do carro é : ", carro.volante.direcao)
    print("A velocidade atual do carro é: ", carro.motor.velocidade)



