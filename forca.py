from unicodedata import normalize

class Fc():

    def __init__(self, **kwargs):
        self.quantidade_de_erros = 0
        self.quantidade_de_acertos = 0
        self.letras_erradas = []
        self.letras_certas = []
        self.dica = kwargs.get('dica')
        self.palavra = []
        self.palavra_formatada = []
        self.certa = False
        self.errada = False
        self.perdeu = False
        self.venceu = False

    def formatar(self):
        self.palavra_formatada = ['_' for x in self.palavra]

    def tentar(self, letra):
        self.letra = self.remover_acentos(letra)
        self.certa = False
        self.errada = False
        if letra in self.letras_erradas or letra in self.letras_certas:
            return
        if letra not in self.remover_acentos(self.palavra) and letra != '':
            self.errada = True
            self.errou()
            self.salvar(False)
            return

        self.certa = True
        # atualizar a lista da palavra formatada
        self.palavra_formatada = [
            l if letra == self.remover_acentos(l) else self.palavra_formatada[i] for i, l in enumerate(self.palavra)]

        # validar quantas letras foram encontradas, poderia usar o count...
        # mas mantive o padrão do metodo 'acertou' sempre somando de 1 em 1!
        [self.acertou() for l in self.palavra if letra == self.remover_acentos(l)]

        self.salvar(True)
    
    def arriscar(self, palavra):
        self.palavra_tentativa = self.remover_acentos(palavra)

        if str(''.join(self.palavra)).replace(' ', '') == '':
            return

        if self.palavra_tentativa == self.remover_acentos(self.palavra):
            self.palavra_formatada = self.palavra
            self.venceu = True
        else:
            self.quantidade_de_erros = 6
            self.perdeu = True

    def remover_acentos(self, texto):
            palavra_sem_acentos = normalize('NFKD', str(''.join(texto))).encode('ASCII','ignore').decode('ASCII')
            return palavra_sem_acentos
                

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
