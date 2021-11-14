class Fc():

    def __init__(self, **kwargs):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.letras_erradas = []
        self.dica = kwargs.get('dica')
        self.palavra = []
        self.palavra_formatada = []

    def formatar(self):
        self.palavra_formatada = ['_' for x in self.palavra]

    def tentativa(self, letra):
        self.letra = letra
        if letra in self.letras_erradas:
            return
        if letra not in self.palavra:
            self.errou()
            self.salvar()
            return

        # atualizar a lista da palavra formatada
        self.palavra_formatada = [
            letra if letra == l else self.palavra_formatada[i] for i, l in enumerate(self.palavra)]

        # validar quantas letras foram encontradas, poderia usar o count...
        # mas mantive o padrão do metodo 'acertou' sempre somando de 1 em 1!
        [self.acertou() for l in self.palavra if letra == l]

    def errou(self):
        self.quantidade_de_erros += 1
        if self.quantidade_de_erros > 6:
            self.perdeu = True
            self.resetar()

    def acertou(self):
        self.quantidade_de_acertos += 1
        if self.quantidade_de_acertos == len(self.palavra):
            self.venceu = True
            self.resetar()

    def salvar(self):
        self.letras_erradas.append(self.letra)
        print(self.letras_erradas)
    
    def resetar(self):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.letras_erradas = []
        self.dica = ''
        self.palavra = []
        self.palavra_formatada = []


if __name__ == "__main__":
    forca = Fc(palavra='vagalume', dica='musica')
    print(forca.palavra_formatada)
    for l in ['v', 'a', 'l', 'm', 'r', 's','c', 'b', 'e', 'g','u']:
        forca.tentativa(l)
    print(forca.palavra_formatada)
