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

        self.frames = {}

        for f in (gui.Frame_menu, gui.Frame_jogo, gui.Frame_palavra_e_dica, gui.Frame_perdeu_jogo, gui.Frame_venceu_jogo):
            nome_pagina = f.__name__
            frame = f(controller=self)
            self.frames[nome_pagina] = frame
            frame.place(x=0, y=0, width=1080, height=608)

        self.frame_jogo = self.frames["Frame_jogo"]
        self.frame_palavra_e_dica = self.frames["Frame_palavra_e_dica"]

        self.mostrar_frame("Frame_menu")

    def mostrar_frame(self, nome_pagina):
        frame = self.frames[nome_pagina]
        frame.tkraise()
        if nome_pagina == "Frame_jogo":
            self.inicializar_jogo()
        elif nome_pagina == "Frame_palavra_e_dica":
            self.inicializar_escolha_de_palavra_e_dica()
        elif nome_pagina == "Frame_perdeu" or nome_pagina == "Frame_ganhou":
            forca.resetar()

    def inicializar_jogo(self):
        self.frame_jogo.txt_entrada.delete(0, "end")
        self.frame_jogo.txt_entrada.focus_set()

        forca.dica = self.frame_palavra_e_dica.txt_dica.get()
        self.frame_jogo.txt_dica.delete(0, "end")
        self.frame_jogo.txt_dica.insert(0, forca.dica)

        forca.palavra = self.frame_palavra_e_dica.palavra
        forca.formatar()
        self.frame_jogo.txt_palavra.delete(0, "end")
        self.frame_jogo.txt_palavra.insert(0, forca.palavra_formatada)

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
