import tkinter as tk


class WindowSelect:

    def __init__(self):
        self.select_window = tk.Tk()
        self.select_window.title("Escolha")
        self._butons()
        self._messages()
        self.select_window.mainloop()

    def open_import_window(self):
        from ContabilidadePYVL.SimplesNacional.windows.import_window import Window_import
        self.select_window.destroy()
        self.import_window = Window_import()

    def open_write_window(self):
        from ContabilidadePYVL.SimplesNacional.windows import write_window
        self.select_window.destroy()
        self.write_window = write_window.Window_write()

    def back_main_window(self):
        from ContabilidadePYVL.windows.main_window import Main_window
        self.select_window.destroy()
        self.main_window = Main_window()

    def _butons(self):
        btn_back = tk.Button(self.select_window, text="<-", command=self.back_main_window)
        btn_back.grid(row=0, column=0,sticky="NW")

        btn_import = tk.Button(self.select_window, text="Importar Planilha", command=self.open_import_window)
        btn_import.grid(row=2, column=0)

        btn_write = tk.Button(self.select_window, text="Digitar Faturamento", command=self.open_write_window)
        btn_write.grid(row=2, column=1)

    def _messages(self):
        mensagem = tk.Label(self.select_window,text="Você prefere digitar o faturamento manualmente ou importar um arquivo XLSX (Planilha Excel)?")
        mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
