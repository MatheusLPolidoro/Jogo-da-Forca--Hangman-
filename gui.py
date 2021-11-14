import tkinter as tk
from tkinter.constants import CENTER
import os

pasta_app = os.path.dirname(__file__) + "\\images\\"
quantidade_de_erros = 0

# --> cores pré selecionadas:
fundo_escuro = "#212121"
branco = "#fff"
verde = "#9cc814"
vermelho = "#f83030"
marrom = "#f7b239"

class Frame_menu(tk.Frame):

    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.configure(background=fundo_escuro)

        self.img_forca_logo = tk.PhotoImage(file=pasta_app + "forca_logo.png")
        self.lb_forca_logo = tk.Label(self,
                                      image=self.img_forca_logo,
                                      background=fundo_escuro
                                      ).place(x=750, y=150)

        self.lb_titulo_jogo = tk.Label(self,
                                       text="Jogo da Forca",
                                       background=fundo_escuro,
                                       foreground=marrom,
                                       anchor=tk.CENTER,
                                       font="Corbel 70 italic"
                                       ).place(x=50, y=160, width=600)

        self.btn_digitar_palavra = tk.Button(self,
                                             text="Digitar Palavra",
                                             command=lambda: controller.mostrar_frame(
                                                 "Frame_palavra_e_dica"),
                                             font="Corbel 30 italic",
                                             background=fundo_escuro,
                                             activebackground=fundo_escuro,
                                             borderwidth=0,
                                             foreground=branco,
                                             activeforeground=verde
                                             ).place(x=40, y=280, width=300, height=60)

        self.btn_sortear_palavra = tk.Button(self,
                                             text="Sortear Palavra",
                                             command=lambda:
                                             controller.mostrar_frame(
                                                 "Frame_jogo"),
                                             font="Corbel 30 italic",
                                             background=fundo_escuro,
                                             activebackground=fundo_escuro,
                                             borderwidth=0,
                                             foreground=branco,
                                             activeforeground=verde
                                             ).place(x=350, y=280, width=300, height=60)

        self.btn_sair_do_jogo = tk.Button(self,
                                          text="Sair do Jogo",
                                          command=lambda: self.sair_jogo(),
                                          font="Corbel 30 italic",
                                          background=fundo_escuro,
                                          activebackground=fundo_escuro,
                                          borderwidth=0,
                                          foreground=branco,
                                          activeforeground=vermelho
                                          ).place(x=190, y=350, width=300, height=60)

        self.lb_autor = tk.Label(self,
                                 text="By: MatheusLPolidoro",
                                 background=fundo_escuro,
                                 foreground=branco,
                                 anchor=tk.CENTER,
                                 font="Corbel 18 italic"
                                 ).place(x=710, y=520, width=300, height=60)

    def sair_jogo(self):
        self.quit()


class Frame_palavra_e_dica(tk.Frame):

    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.configure(background=fundo_escuro)

        self.palavra = []

        self.lb_dica = tk.Label(self,
                                text="Digite a dica",
                                anchor=tk.CENTER,
                                foreground=branco,
                                background=fundo_escuro,
                                font="corbel 24 italic"
                                ).place(relx=.5, rely=.25, anchor="center")

        self.txt_dica = tk.Entry(self,
                                 background=fundo_escuro,
                                 foreground=branco,
                                 font=("Corbel", 24, "italic"),
                                 justify=tk.CENTER,
                                 borderwidth=0,
                                 highlightcolor=verde,
                                 highlightbackground=branco,
                                 highlightthickness=3,
                                 insertofftime=800,
                                 insertbackground=verde,
                                 insertwidth=3
                                 )
        self.txt_dica.place(relx=.5,
                            rely=.35,
                            anchor="center",
                            height=60,
                            width=500
                            )
        self.txt_dica.bind("<Key>", self.formatar_entrada_dica)

        self.img_valido = tk.PhotoImage(file=pasta_app + "valido.png")
        self.img_invalido = tk.PhotoImage(file=pasta_app + "invalido.png")

        self.lb_valicao_dica = tk.Label(self,
                                        background=fundo_escuro
                                        )
        self.lb_valicao_dica.place(relx=.765,
                                   rely=.35,
                                   anchor=CENTER,
                                   height=60,
                                   width=60
                                   )

        self.lb_palavra = tk.Label(self,
                                   text="Digite a palavra",
                                   anchor=tk.CENTER,
                                   foreground=branco,
                                   background=fundo_escuro,
                                   font="corbel 24 italic"
                                   ).place(relx=.5, rely=.45, anchor="center")

        self.txt_palavra = tk.Entry(self,
                                    background=fundo_escuro,
                                    foreground=branco,
                                    font=("corbel", 30, "bold"),
                                    justify=tk.CENTER,
                                    borderwidth=0,
                                    highlightcolor=verde,
                                    highlightbackground=branco,
                                    highlightthickness=3,
                                    insertofftime=800,
                                    insertbackground=verde,
                                    insertwidth=3
                                    )
        self.txt_palavra.place(relx=.5,
                               rely=.55,
                               anchor="center",
                               height=60,
                               width=700
                               )
        self.txt_palavra.bind("<Key>", self.formatar_entrada_palavra)

        self.lb_valicao_palavra = tk.Label(self,
                                           background=fundo_escuro,
                                           )
        self.lb_valicao_palavra.place(relx=.858,
                                      rely=.55,
                                      anchor=CENTER,
                                      height=60,
                                      width=60
                                      )

        self.img_voltar = tk.PhotoImage(file=pasta_app + "voltar_escolha.png")
        self.img_opcao = tk.Label(self,
                                  image=self.img_voltar,
                                  background=fundo_escuro
                                  ).place(x=880, y=520)

        self.btn_opcao = tk.Button(self,
                                   text="Voltar",
                                   command=lambda: controller.mostrar_frame(
                                       "Frame_menu"),
                                   font="Corbel 20 italic",
                                   background=fundo_escuro,
                                   activebackground=fundo_escuro,
                                   borderwidth=0,
                                   foreground=verde,
                                   activeforeground=branco
                                   ).place(x=940, y=520, width=100, height=60)

        tk.Frame(self,
                 width=223,
                 height=69,
                 background=verde,
                 highlightbackground=verde,
                 highlightthickness=0
                 ).place(relx=.5, rely=.78, anchor="center")
        self.btn_comecar_jogo = tk.Button(self,
                                          text="Começar o Jogo",
                                          command=self.validar_dica_e_palavra,
                                          font="corbel 22 italic bold",
                                          background=fundo_escuro,
                                          activebackground=fundo_escuro,
                                          foreground=verde,
                                          activeforeground=branco,
                                          borderwidth=0,
                                          highlightthickness=3,
                                          ).place(relx=.5, rely=.78, anchor="center")

    def formatar_entrada_dica(self, event=None):
        self.txt_dica.config(highlightbackground=branco,
                             insertbackground=verde)

        charact = event.char.upper().strip()

        texto_limite = self.txt_dica.get()[:25] + charact
        texto_limite = texto_limite.strip()

        if event.keysym.upper() == "BACKSPACE":
            texto_limite = texto_limite[:-2]
        elif event.keysym.upper() == "RETURN":
            self.txt_palavra.focus_set()
            return "break"
        elif event.keysym.upper() == "ESCAPE":
            return "break"
        elif event.keysym.upper() == "SCPACE":
            return

        if not texto_limite.replace(' ', '').isalpha() and len(texto_limite) > 0:
            self.lb_valicao_dica.config(image=self.img_invalido)
            self.txt_dica.config(highlightcolor=vermelho,
                                 insertbackground=vermelho)
        elif len(texto_limite) == 0 or len(texto_limite) == 0 and event.keysym.upper() == "TAB":
            self.lb_valicao_dica.config(image='')
            self.txt_dica.config(highlightcolor=verde,
                                 insertbackground=verde)
        else:
            if event.keysym.upper() != "SPACE":
                self.lb_valicao_dica.config(image=self.img_valido)
                self.txt_dica.config(highlightcolor=verde,
                                     insertbackground=verde)

        if len(event.keysym) > 1:
            return
        else:
            self.txt_dica.delete(0, "end")
            self.txt_dica.insert(0, texto_limite)
        return "break"

    def max_caracteres(self, max):
        texto_limite = self.txt_palavra.get()[:max] + '_ '
        self.txt_palavra.delete(0, "end")
        self.txt_palavra.insert(0, texto_limite)
        if len(self.palavra) > 23:
            self.palavra.pop()

    def formatar_entrada_palavra(self, event=None):
        self.upper_case = event.keysym.upper()
        self.lb_valicao_palavra.config(image='')
        self.txt_palavra.config(highlightbackground=branco)

        if event.keysym.lower() == "backspace" and len(self.palavra) > 0:
            self.palavra.pop()
            inicio = len(self.txt_palavra.get()) - 2
            self.txt_palavra.delete(inicio, "end")
            return "break"
        if len(event.keysym) == 1 and event.keysym not in '0123456789':
            self.max_caracteres(46)
            self.palavra.append(self.upper_case)
            print(self.palavra)
        return "break"

    def validar_dica_e_palavra(self):
        self.lb_valicao_dica.focus()
        dica = self.txt_dica.get().replace(' ','')
        palavra = self.txt_palavra.get()
        dica_valida = palavra_valida = False
        if not dica.isalpha():
            self.lb_valicao_dica.config(image=self.img_invalido)
            self.txt_dica.config(highlightbackground=vermelho,
                                 highlightcolor=vermelho,
                                 insertbackground=vermelho)
        else:
            self.lb_valicao_dica.config(image=self.img_valido)
            self.txt_dica.config(highlightbackground=verde,
                                 highlightcolor=verde,
                                 insertbackground=verde)
            dica_valida = True

        if len(palavra) == 0:
            self.lb_valicao_palavra.config(image=self.img_invalido)
            self.txt_palavra.config(highlightbackground=vermelho,
                                    highlightcolor=vermelho,
                                    insertbackground=vermelho)
        else:
            self.lb_valicao_palavra.config(image=self.img_valido)
            self.txt_palavra.config(highlightbackground=verde,
                                    highlightcolor=verde,
                                    insertbackground=verde)
            palavra_valida = True

        if dica_valida == True and palavra_valida == True:
            self.after(
                1000, lambda: self.controller.mostrar_frame("Frame_jogo"))


class Frame_jogo(tk.Frame):

    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.configure(background=fundo_escuro)

        self.img_forca = tk.PhotoImage(file=pasta_app + "forca_0.png")
        self.lb_forca = tk.Label(self,
                                 image=self.img_forca,
                                 background=fundo_escuro
                                 )
        self.lb_forca.place(x=454, y=102)

        self.txt_dica = tk.Entry(self,
                                 background=fundo_escuro,
                                 justify=tk.CENTER,
                                 foreground=branco,
                                 font="Corbel 24 italic",
                                 borderwidth=0,
                                 insertontime=0
                                 )

        # => incluir váriavel que ira guardar a dica da palavra
        self.txt_dica.bind("<Key>", self.posicionar_cursor)
        self.txt_dica.place(x=40, y=50, width=1000)

        self.txt_palavra = tk.Entry(self,
                                    background=fundo_escuro,
                                    justify=tk.CENTER,
                                    foreground=branco,
                                    font="Corbel 43 italic",
                                    borderwidth=0,
                                    insertontime=0
                                    )

        # => a validação da tecla <enter> deve acionar função do botão "enviar" (modificar qtd erros e qtd acertos)
        self.txt_palavra.bind("<Key>", self.posicionar_cursor)
        self.txt_palavra.place(x=40, y=300, width=1000)

        self.lb_letras_erradas = tk.Label(self,
                                          # => o resultado da funcão de validação da letra pode alterar esse valor
                                          text='a  b  c  d  e  f  g',
                                          background=fundo_escuro,
                                          foreground=vermelho,
                                          anchor=tk.CENTER,
                                          font="Corbel 20 italic"
                                          ).place(x=40, y=370, width=1000)

        self.txt_entrada = tk.Entry(self,
                                    background="#383b37",
                                    justify=tk.CENTER,
                                    foreground="#cbceff",
                                    font="Corbel 35",
                                    borderwidth=0,
                                    insertontime=0
                                    )

        self.txt_entrada.place(relx=.5, rely=.73, width=100, anchor="center")
        self.txt_entrada.bind("<Key>", self.limitar_entrada)

        self.enviar_btn = tk.Button(self,
                                    text="Enviar",
                                    command=lambda: controller.mostrar_frame(
                                        "Frame_jogo"),
                                    font="corbel 15 italic bold",
                                    width=12,
                                    background="#1a7420",
                                    activebackground=verde,
                                    foreground=branco,
                                    activeforeground=fundo_escuro,
                                    borderwidth=0,
                                    highlightthickness=3,
                                    ).place(relx=.5, rely=.85, anchor="center")

        self.img_trevo = tk.PhotoImage(
            file=pasta_app + "trevo_de_quatro_folhas.png")
        self.img_voltar = tk.PhotoImage(file=pasta_app + "voltar_escolha.png")
        self.img_opcao_arriscar = tk.Label(self,
                                           image=self.img_trevo,
                                           background=fundo_escuro
                                           )
        self.img_opcao_arriscar.place(x=880, y=520)

        self.btn_opcao = tk.Button(self,
                                   text="Arriscar",
                                   command=self.arriscar_palavra,
                                   font="Corbel 20 italic",
                                   background=fundo_escuro,
                                   activebackground=fundo_escuro,
                                   borderwidth=0,
                                   foreground=verde,
                                   activeforeground=branco
                                   )
        self.btn_opcao.place(x=940, y=520, width=100, height=60)

        self.img_skull = tk.PhotoImage(file=pasta_app + "desistir.png")
        self.img_opcao_desistir = tk.Label(self,
                                           image=self.img_skull,
                                           background=fundo_escuro
                                           ).place(x=40, y=520)

        self.btn_desistir = tk.Button(self,
                                      text="Desistir",
                                      command=lambda: controller.mostrar_frame(
                                          "Frame_perdeu_jogo"),
                                      font="Corbel 20 italic",
                                      background=fundo_escuro,
                                      activebackground=fundo_escuro,
                                      borderwidth=0,
                                      foreground=vermelho,
                                      activeforeground=branco
                                      ).place(x=110, y=520, width=100, height=60)

    def arriscar_palavra(self):

        if self.txt_entrada.winfo_width() == 100:
            background = "#212125"
            foreground = verde
            width = 1000
            self.img_opcao_arriscar.config(image=self.img_voltar)
            self.btn_opcao.config(text="Voltar")
        else:
            background = "#383b37"
            foreground = "#cbceff"
            width = 100
            self.img_opcao_arriscar.config(image=self.img_trevo)

        self.txt_entrada.config(background=background, foreground=foreground)
        self.txt_entrada.place_configure(relx=.5, width=width, anchor="center")
        self.txt_entrada.delete(0, "end")

    def posicionar_cursor(self, event=None):

        self.txt_entrada.focus_set()
        if self.txt_entrada.winfo_width() == 100:
            self.txt_entrada.delete(0, "end")
        self.txt_entrada.insert("end", event.char.upper())
        return "break"

    def max_caracteres(self, max):
        texto_limite = self.txt_entrada.get()[:max] + self.upper_case
        self.txt_entrada.delete(0, "end")
        self.txt_entrada.insert(0, texto_limite)

    def limitar_entrada(self, event=None):
        self.upper_case = event.keysym.upper()
        if event.keysym.lower() == "backspace":
            return
        if self.txt_entrada.winfo_width() == 100 and len(event.keysym) == 1 and event.keysym not in '0123456789':
            self.max_caracteres(0)
            return "break"
        if len(event.keysym) == 1 and event.keysym not in '0123456789':
            self.max_caracteres(23)
            return "break"
        return "break"


class Frame_perdeu_jogo(tk.Frame):

    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.configure(background=fundo_escuro)

        self.img_perdeu = tk.PhotoImage(file=pasta_app + "img_perdeu.png")
        self.lb_perdeu = tk.Label(self,
                                  image=self.img_perdeu,
                                  background=fundo_escuro
                                  )
        self.lb_perdeu.place(relx=.5, rely=.3, anchor="center")

        self.lb_msg_perdeu = tk.Label(self,
                                      text="Você PERDEU...",
                                      font="corbel 60 italic",
                                      background=fundo_escuro,
                                      foreground=branco,
                                      ).place(relx=.1, rely=.6, anchor="w")

        self.lb_msg_palavra = tk.Label(self,
                                       text="A palavra é ",
                                       font="corbel 23",
                                       background=fundo_escuro,
                                       foreground=branco
                                       ).place(relx=.12, rely=.7, anchor="w")

        tk.Frame(self,
                 background=branco,
                 width=5,
                 height=115
                 ).place(relx=.08, rely=.55)

        self.btn_menu = tk.Button(self,
                                  text="Menu",
                                  command=lambda: controller.mostrar_frame(
                                      "Frame_menu"),
                                  font="Corbel 20 italic bold",
                                  background=fundo_escuro,
                                  activebackground=fundo_escuro,
                                  borderwidth=0,
                                  foreground=branco,
                                  activeforeground=marrom
                                  )
        self.btn_menu.place(x=600, y=520, width=100, height=60)

        self.btn_jogar_novamente = tk.Button(self,
                                             text="Jogar Novamente",
                                             command=lambda: controller.mostrar_frame(
                                                 "Frame_palavra_e_dica"),
                                             font="Corbel 20 italic bold",
                                             background=fundo_escuro,
                                             activebackground=fundo_escuro,
                                             borderwidth=0,
                                             foreground=branco,
                                             activeforeground=marrom
                                             )
        self.btn_jogar_novamente.place(x=750, y=520, width=210, height=60)


class Frame_venceu_jogo(tk.Frame):

    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller

        self.img_bg = tk.PhotoImage(file=pasta_app + "backgroud_venceu.png")
        self.lb_bg = tk.Label(self,
                              image=self.img_bg,
                              background=fundo_escuro
                              ).place(x=0, y=0, width=1080, height=608)

        self.lb_msg_venceu = tk.Label(self,
                                      text="Você VENCEU!",
                                      background=fundo_escuro,
                                      foreground=branco,
                                      font="corbel 60 italic"
                                      ).place(relx=.5, rely=.5, anchor="center")

        self.lb_msg_palavra = tk.Label(self,
                                       text="A palavra é ",
                                       background=fundo_escuro,
                                       foreground=branco,
                                       font="corbel 23 italic"
                                       ).place(relx=.5, rely=.6, anchor="center")

        self.btn_menu = tk.Button(self,
                                  text="Menu",
                                  command=lambda: controller.mostrar_frame(
                                      "Frame_menu"),
                                  font="Corbel 20 italic bold",
                                  background=fundo_escuro,
                                  activebackground=fundo_escuro,
                                  borderwidth=0,
                                  foreground=branco,
                                  activeforeground=marrom
                                  )
        self.btn_menu.place(x=600, y=520, width=100, height=60)

        self.btn_jogar_novamente = tk.Button(self,
                                             text="Jogar Novamente",
                                             command=lambda: controller.mostrar_frame(
                                                 "Frame_jogo"),
                                             font="Corbel 20 italic bold",
                                             background=fundo_escuro,
                                             activebackground=fundo_escuro,
                                             borderwidth=0,
                                             foreground=branco,
                                             activeforeground=marrom
                                             )
        self.btn_jogar_novamente.place(x=750, y=520, width=210, height=60)
