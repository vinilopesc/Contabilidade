import tkinter as tk
import Constantes
from PIL import Image, ImageTk

class Main_window:

    def __init__(self):
        self.window_main = tk.Tk()
        self.window_main.title("Contabilidade PYVL")
        self._mensagens()
        self._botoes()
        self.images()
        self.style()
        self.window_main.mainloop()
    def open_select_window(self):
        from SimplesNacional.windows.select_window import WindowSelect
        self.window_main.destroy()
        self.window_select = WindowSelect()

    def style(self):
        self.window_main.configure(bg=Constantes.bck_color)

    def _mensagens(self):
        msg_PYVL = tk.Label(self.window_main, text="Sistema contábil PYVL ", font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        msg_PYVL.grid(row=0, column=0, columnspan=6, sticky="nsew")

        msg_imposto = tk.Label(self.window_main, text="Selecione o imposto => ",  font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        msg_imposto.grid(row=1, column=0)

        msg_email = tk.Label(self.window_main, text="pyvldevops@gmail.com", font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        msg_email.grid(row=2, column=0, sticky="w", padx=30)

        msg_insta = tk.Label(self.window_main, text="pyvl_devops", font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        msg_insta.grid(row=3, column=0, sticky='w', padx=30)

        msg_wpp = tk.Label(self.window_main, text="(38) 99182-8365", font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        msg_wpp.grid(row=4, column=0, sticky='w', padx=30)

    def images(self):
        new_large = 30
        new_heigh = 30

        img_email = Image.open("email.png")
        new_img_insta = img_email.resize((new_large, new_heigh))
        self.email_img = ImageTk.PhotoImage(new_img_insta)
        label_email = tk.Label(self.window_main, image=self.email_img, background=Constantes.bck_color)
        label_email.grid(row=2, column=0, sticky="w")

        img_insta = Image.open("insta.png")
        new_img_insta = img_insta.resize((new_large, new_heigh))
        self.insta_img = ImageTk.PhotoImage(new_img_insta)
        label_insta = tk.Label(self.window_main, image=self.insta_img, background=Constantes.bck_color)
        label_insta.grid(row=3, column=0, sticky="w")

        img_wpp = Image.open("wpp.png")
        new_img_wpp = img_wpp.resize((new_large, new_heigh))
        self.wpp_img = ImageTk.PhotoImage(new_img_wpp)
        label_com_imagem = tk.Label(self.window_main, image=self.wpp_img, background=Constantes.bck_color)
        label_com_imagem.grid(row=4, column=0, sticky="w")


    def _botoes(self):
        btn_simples_nacional = tk.Button(self.window_main, text="Simples Nacional", command=self.open_select_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_simples_nacional.grid(row=1, column=1, sticky='nsew')
