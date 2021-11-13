class Fc():

    def __init__(self, **kwargs):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.dica_palavra = kwargs.get('dica')
        self.palavra_principal = kwargs.get('palavra')

    def errou(self):
        self.quantidade_de_erros += 1
        print(self.quantidade_de_erros)

    def acertou(self):
        self.quantidade_de_acertos += 1
        print(self.quantidade_de_acertos)

    def salvar(self, letra):
        self.letras_erradas = letra


if __name__ == "__main__":
    teste_forca = Fc(dica='musica', palavra='vagalume')

    print(teste_forca.dica_palavra, teste_forca.palavra_principal,
          teste_forca.acerto(), teste_forca.erro())
