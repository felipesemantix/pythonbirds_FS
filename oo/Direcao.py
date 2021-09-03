class Direcao:

    def __init__(self, direcao="N", giro=0):
        self.direcao = direcao
        self.giro = giro

    def posicao(self, direcao_giro):
        posicoes = ['N', 'L', 'S', 'O']
        if direcao_giro > 0:
            if self.direcao != 'O':
                self.giro += direcao_giro
                self.direcao = posicoes[self.giro]
            else:
                self.direcao = 'N'
                self.giro = 0
        elif direcao_giro < 0:
            if self.direcao != 'N':
                self.giro += direcao_giro
                self.direcao = posicoes[self.giro]
            else:
                self.direcao = 'O'
                self.giro = 3
        else:
            pass

    def girar_direta(self):
        self.posicao(1)

    def girar_esquerda(self):
        self.posicao(-1)
