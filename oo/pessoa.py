class Pessoa:
    def __init__(self, nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Felipe')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
