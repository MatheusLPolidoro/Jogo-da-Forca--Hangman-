class Fc():

    def __init__(self, **kwargs):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.letras_erradas = []
        self.letras_certas = []
        self.dica = kwargs.get('dica')
        self.palavra = []
        self.palavra_formatada = []
        self.perdeu = False
        self.venceu = False

    def formatar(self):
        self.palavra_formatada = ['_' for x in self.palavra]

    def tentar(self, letra):
        self.letra = letra
        if letra in self.letras_erradas or letra in self.letras_certas:
            return
        if letra not in self.palavra and letra != '':
            self.errou()
            self.salvar(False)
            return

        # atualizar a lista da palavra formatada
        self.palavra_formatada = [
            letra if letra == l else self.palavra_formatada[i] for i, l in enumerate(self.palavra)]

        # validar quantas letras foram encontradas, poderia usar o count...
        # mas mantive o padrão do metodo 'acertou' sempre somando de 1 em 1!
        [self.acertou() for l in self.palavra if letra == l]

        self.salvar(True)

    def arriscar(self, palavra):
        self.palavra_tentativa = palavra

        if str(''.join(self.palavra)).replace(' ', '') == '':
            return

        if list(self.palavra_tentativa) == self.palavra:
            self.venceu = True
        else:
            self.quantidade_de_erros = 6
            self.perdeu = True

    def errou(self):
        self.quantidade_de_erros += 1
        if self.quantidade_de_erros == 6:
            self.perdeu = True

    def acertou(self):
        self.quantidade_de_acertos += 1
        if self.quantidade_de_acertos == len(self.palavra):
            self.venceu = True

    def salvar(self, acerto):
        if self.letra != '' and acerto == False:
            self.letras_erradas.append(self.letra)
        elif self.letra != '' and acerto == True:
            self.letras_certas.append(self.letra)

    def resetar(self):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.letras_erradas = []
        self.letras_certas = []
        self.dica = ''
        self.palavra = []
        self.palavra_formatada = []
