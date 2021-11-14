import tkinter as tk
import gui
import forca as fc

forca = fc.Fc()


class mostrar_app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Jogo da Forca")
        self.geometry("1080x608")
        self.resizable(width=0, height=0)
        self.iconbitmap(gui.pasta_app + 'forca_icone.ico')
        self.img_forca_controle = 0

        self.frames = {}

        for f in (gui.Frame_jogo, gui.Frame_palavra_e_dica, gui.Frame_perdeu_jogo, gui.Frame_venceu_jogo, gui.Frame_menu,):
            nome_pagina = f.__name__
            frame = f(controle=self, jogo=forca)
            frame.place(x=0, y=0, width=1080, height=608)
            self.frames[nome_pagina] = frame

        self.frame_jogo = self.frames["Frame_jogo"]
        self.frame_palavra_e_dica = self.frames["Frame_palavra_e_dica"]
        self.frame_venceu_jogo = self.frames["Frame_venceu_jogo"]
        self.frame_perdeu_jogo= self.frames["Frame_perdeu_jogo"]

        self.mostrar_frame("Frame_menu")

    def mostrar_frame(self, nome_pagina):
        frame = self.frames[nome_pagina]

        if nome_pagina == "Frame_jogo":
            self.inicializar_jogo()
        elif nome_pagina == "Frame_palavra_e_dica":
            self.inicializar_escolha_de_palavra_e_dica()
        elif nome_pagina == "Frame_perdeu_jogo" or nome_pagina == "Frame_venceu_jogo":
            self.frame_venceu_jogo.lb_msg_palavra.config(
                text="A palavra é " + ''.join(self.frame_palavra_e_dica.palavra))
            self.frame_perdeu_jogo.lb_msg_palavra.config(
                text="A palavra é " + ''.join(self.frame_palavra_e_dica.palavra))
            self.frame_jogo.forca.resetar()

        frame.tkraise()

    def inicializar_jogo(self):
        self.frame_jogo.canvas.delete("all")
        self.frame_jogo.canvas.create_image(
            0, 0, image=self.frame_jogo.img_forca[0], anchor=tk.NW)

        self.frame_jogo.txt_entrada.delete(0, "end")
        self.frame_jogo.txt_entrada.focus_set()

        self.frame_jogo.lb_letras_erradas.config(text='')

        forca.dica = self.frame_palavra_e_dica.txt_dica.get()
        self.frame_jogo.txt_dica.delete(0, "end")
        self.frame_jogo.txt_dica.insert(0, forca.dica)

        forca.palavra = self.frame_palavra_e_dica.palavra
        forca.formatar()
        self.frame_jogo.txt_palavra.delete(0, "end")
        self.frame_jogo.txt_palavra.insert(0, forca.palavra_formatada)

        self.frame_jogo.modo_letra()

        self.frame_jogo.update()

    def inicializar_escolha_de_palavra_e_dica(self):
        self.frame_palavra_e_dica.lb_valicao_dica.config(image='')
        self.frame_palavra_e_dica.lb_valicao_palavra.config(image='')

        self.frame_palavra_e_dica.txt_dica.delete(0, "end")
        self.frame_palavra_e_dica.txt_palavra.delete(0, "end")

        self.frame_palavra_e_dica.palavra.clear()
        self.frame_palavra_e_dica.txt_dica.focus_set()


if __name__ == "__main__":
    app = mostrar_app()
    app.mainloop()
