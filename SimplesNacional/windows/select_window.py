import tkinter as tk
import Constantes

class WindowSelect:

    def __init__(self):
        self.select_window = tk.Tk()
        self.select_window.title("Escolha")
        self._butons()
        self._messages()
        self.style()
        self.select_window.mainloop()

    def style(self):
        self.select_window.configure(bg=Constantes.bck_color)

    def open_import_window(self):
        from SimplesNacional.windows.import_window import Window_import
        self.select_window.destroy()
        self.import_window = Window_import()

    def open_write_window(self):
        from SimplesNacional.windows.write_window import Window_write
        self.select_window.destroy()
        self.write_window = Window_write()

    def back_main_window(self):
        from SimplesNacional.windows.main_window import Main_window
        self.select_window.destroy()
        self.main_window = Main_window()

    def _butons(self):
        btn_back = tk.Button(self.select_window, text="<-", command=self.back_main_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_back.grid(row=0, column=0,sticky="NW")

        btn_import = tk.Button(self.select_window, text="Importar Planilha", command=self.open_import_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_import.grid(row=2, column=0)

        btn_write = tk.Button(self.select_window, text="Digitar Faturamento", command=self.open_write_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_write.grid(row=2, column=1)

    def _messages(self):
        mensagem = tk.Label(self.select_window,text="Você prefere digitar o faturamento manualmente ou importar um arquivo XLSX (Planilha Excel)?",font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
