import tkinter as tk
import gui
import forca as fc
import consulta as con
from random import choice as escolha
import pygame as pg

forca = fc.Fc()
pg.mixer.init()

class mostrar_app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.id_dica_anterior = None
        self.iniciar_banco()
        self.sorteio = False

        self.title("Jogo da Forca")
        self.geometry("1080x608")
        self.resizable(width=0, height=0)
        self.iconbitmap(gui.pasta_app + 'forca_icone.ico')
        self.img_forca_controle = 0
        self.tela_jogar_novamente = ""
        self.dificuldade = ""

        self.frames = {}

        for f in (gui.Frame_jogo,
                  gui.Frame_palavra_e_dica,
                  gui.Frame_perdeu_jogo,
                  gui.Frame_venceu_jogo,
                  gui.Frame_menu,
                  gui.Frame_dificuldade):
            nome_pagina = f.__name__
            frame = f(controle=self, jogo=forca)
            frame.place(x=0, y=0, width=1080, height=608)
            self.frames[nome_pagina] = frame

        self.frame_jogo = self.frames["Frame_jogo"]
        self.frame_palavra_e_dica = self.frames["Frame_palavra_e_dica"]
        self.frame_dificuldade = self.frames["Frame_dificuldade"]
        self.frame_venceu_jogo = self.frames["Frame_venceu_jogo"]
        self.frame_perdeu_jogo = self.frames["Frame_perdeu_jogo"]

        self.mostrar_frame("Frame_menu", None)

    def mostrar_frame(self, nome_pagina, som):
        if nome_pagina == 'Jogar_novamente' and self.tela_jogar_novamente != "repetir":
            self.after(200, self.play(som))
            nome_pagina = self.tela_jogar_novamente
        elif nome_pagina == 'Jogar_novamente' and self.tela_jogar_novamente == "repetir":
            nome_pagina = "Frame_jogo"
        else:
            self.after(200, self.play(som))

        frame = self.frames[nome_pagina]

        if nome_pagina == "Frame_jogo":
            self.inicializar_jogo()
        elif nome_pagina == "Frame_palavra_e_dica":
            self.inicializar_escolha_de_palavra_e_dica()
            self.tela_jogar_novamente = nome_pagina
        elif nome_pagina == "Frame_dificuldade":
            self.tela_jogar_novamente = "Frame_jogo"
        elif nome_pagina == "Frame_perdeu_jogo" or nome_pagina == "Frame_venceu_jogo":
            if self.sorteio == False:
                self.frame_venceu_jogo.lb_msg_palavra.config(
                    text="A palavra é " + ''.join(self.frame_palavra_e_dica.palavra))
                self.frame_perdeu_jogo.lb_msg_palavra.config(
                    text="A palavra é " + ''.join(self.frame_palavra_e_dica.palavra))
            else:
                self.frame_venceu_jogo.lb_msg_palavra.config(
                    text="A palavra é " + ''.join(self.palavra))
                self.frame_perdeu_jogo.lb_msg_palavra.config(
                    text="A palavra é " + ''.join(self.palavra))
                self.sorteio = False
            self.frame_jogo.forca.resetar()

        frame.tkraise()

    def inicializar_jogo(self):
        if self.tela_jogar_novamente == "Frame_jogo":
            self.tela_jogar_novamente = "repetir"
        elif self.tela_jogar_novamente == "repetir":
            self.tela_jogar_novamente = "Frame_jogo"
            self.frame_dificuldade.selecao_dificuldade(self.dificuldade)

        self.frame_jogo.canvas.delete("all")
        self.frame_jogo.canvas.create_image(
            0, 0, image=self.frame_jogo.img_forca[0], anchor=tk.NW)

        self.frame_jogo.txt_entrada.delete(0, "end")
        self.frame_jogo.txt_entrada.focus_set()

        self.frame_jogo.lb_letras_erradas.config(text='')

        if self.sorteio == False:
            self.frame_jogo.lb_dificuldade.config(text="")
            forca.dica = self.frame_palavra_e_dica.txt_dica.get()
            self.frame_jogo.txt_dica.delete(0, "end")
            self.frame_jogo.txt_dica.insert(0, forca.dica)
            forca.palavra = self.frame_palavra_e_dica.palavra
            forca.formatar()
            self.frame_jogo.txt_palavra.delete(0, "end")
            self.frame_jogo.txt_palavra.insert(0, forca.palavra_formatada)
        else:
            forca.dica = self.dica  
            self.frame_jogo.txt_dica.delete(0, "end")
            self.frame_jogo.txt_dica.insert(0, forca.dica)
            forca.palavra = self.palavra
            forca.formatar()
            self.frame_jogo.txt_palavra.delete(0, "end")
            self.frame_jogo.txt_palavra.insert(0, forca.palavra_formatada)
            self.frame_jogo.lb_dificuldade.config(text=self.dificuldade)

        self.frame_jogo.modo_letra()

        self.frame_jogo.update()

    def inicializar_escolha_de_palavra_e_dica(self):
        self.frame_palavra_e_dica.lb_valicao_dica.config(image='')
        self.frame_palavra_e_dica.lb_valicao_palavra.config(image='')

        self.frame_palavra_e_dica.txt_dica.delete(0, "end")
        self.frame_palavra_e_dica.txt_palavra.delete(0, "end")

        self.frame_palavra_e_dica.palavra.clear()
        self.frame_palavra_e_dica.txt_dica.focus_set()

    def iniciar_banco(self):
        self.banco = con.Db("palavras")
        # atualizar todos os valores de chamada para FALSO.
        self.banco.executar(
            "UPDATE tb_palavra SET B_CHAMADA=0 WHERE B_CHAMADA=1")

        # consultar quantas dicas constam cadastradas.
        self.qtd_dicas = self.banco.consultar("SELECT N_IDDICA FROM tb_dica")

    def sortear_dica(self):
        # sortear uma dica (número inteiro) que seja diferente da dica anterior.
        self.id_dica = escolha(self.qtd_dicas)[0]
        while self.id_dica == self.id_dica_anterior:
            self.id_dica = escolha(self.qtd_dicas)[0]
        # guardar número da dica sorteada para não sortear na próxima rodada
        self.id_dica_anterior = self.id_dica

        self.dica = self.banco.consultar(f"""SELECT T_DICA
            FROM tb_dica WHERE N_IDDICA={self.id_dica};""")

    def sortear_palavra(self):
        self.dificuldade = self.frame_dificuldade.dificuldade

        # consultar palavras com a dica e com a dificuldade escolhida que sejam :
        # DIFERENTES de VERDADEIRO para palavras anteriores.
        consulta_palavra = self.banco.consultar(f"""SELECT N_IDPALAVRA, T_PALAVRA 
        FROM tb_palavra WHERE N_IDDICA={self.id_dica} AND T_DIFICULDADE='{self.dificuldade}' AND B_CHAMADA=0;""")

        try:
            palavra = escolha(consulta_palavra)
            self.id_palavra = palavra[0]
            self.palavra = palavra[1].upper()
        except:
            self.banco.executar(f"""UPDATE tb_palavra SET B_CHAMADA=0 
            WHERE N_IDDICA={self.id_dica} AND T_DIFICULDADE='{self.dificuldade}';""")
            consulta_palavra = self.banco.consultar(f"""SELECT N_IDPALAVRA, T_PALAVRA 
            FROM tb_palavra WHERE N_IDDICA={self.id_dica} AND T_DIFICULDADE='{self.dificuldade}' AND B_CHAMADA=0;""")

        self.banco.executar(f"""UPDATE tb_palavra SET B_CHAMADA=1 
        WHERE N_IDPALAVRA={self.id_palavra};""")
        self.sorteio = True
        self.after(200, self.mostrar_frame("Frame_jogo", "troca_de_tela"))
        print(self.palavra)

    def play(self, arquivo):
        if arquivo != None:
            caminho = gui.pasta_app + "sons\\" + str(arquivo) + ".wav"
            pg.mixer.music.load(caminho)
            pg.mixer.music.play(loops=0)


if __name__ == "__main__":
    app = mostrar_app()
    app.mainloop()
