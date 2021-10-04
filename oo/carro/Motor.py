class Motor:
    """
    Classe que implementa as funções do motor de um carro.

    Params
    velocidade: Int

    """

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def incrementar_velocidade(self, aceleracao=0):
        """
        Método que incrementa a velocidade do motor de acordo
        com a aceleração que foi passada e retorna a velocidade atual.

        Params
        aceleracao: Int

        """
        self.velocidade += aceleracao  # # transmite a aceleração para a velociade atual
        return self.velocidade

    def acelerar(self):
        """
        Método que realiza a aceleração positiva do veículo de modo a
        aumentar a velocidade em uma unidade, retornando o incremento
        para o método incremetar_velocidade()
        """
        self.incrementar_velocidade(1)
        return self.velocidade

    def frear(self):
        """
        Método que realiza a aceleração negativa do veículo de modo a
        diminuir a velocidade em duas unidades com o limite de velocidade
        igual a zero, retornando o decremento para o método
        incremetar_velocidade()

        """
        if self.velocidade <= 0:  # Se o carro não estiver em movimento não altera a aceleração
            aceleracao = 0
        elif self.velocidade == 1:  # se a velocidade igual a 1 diminui a mesma em uma undidade só
            aceleracao = -1
        elif self.velocidade >= 2:
            aceleracao = -2
        self.incrementar_velocidade(aceleracao)
        return self.velocidade
