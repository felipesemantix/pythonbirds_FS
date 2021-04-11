class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    thiago = Pessoa(nome='Thiago')
    sidney = Pessoa(nome='Sidney')
    paulo = Pessoa(nome='Paulo')
    nivaldo = Pessoa(felipe, thiago, sidney, paulo, nome="Nivaldo", idade=64)
    print(nivaldo.cumprimentar())
    print(nivaldo.nome)
    print(nivaldo.idade)
    for filho in nivaldo.filhos:
        print(filho.nome)
    print(nivaldo.__dict__)
