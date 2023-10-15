import tkinter as tk


class Main_window:

    def __init__(self):
        self.window_SN = tk.Tk()
        self.window_SN.title("Contabilidade PYVL")
        self._mensamgens()
        self._botoes()
        self.window_SN.mainloop()
    def open_select_window(self):
        from ContabilidadePYVL.SimplesNacional.windows.select_window import WindowSelect
        self.window_SN.destroy()
        self.window_select = WindowSelect()

    def _mensamgens(self):
        mensagem_imposto = tk.Label(self.window_SN, text="Selecione o imposto => ", font=14)
        mensagem_imposto.grid(row=1, column=0, sticky='w')

    def _botoes(self):
        btn_simples_nacional = tk.Button(self.window_SN, text="Simples Nacional", command=self.open_select_window)
        btn_simples_nacional.grid(row=1, column=1)

        btn_iof = tk.Button(self.window_SN, text="IOF")
        btn_iof.grid(row=1, column=2)

        btn_irf = tk.Button(self.window_SN, text="IRF")
        btn_irf.grid(row=1, column=3)

        btn_pasep = tk.Button(self.window_SN, text="PASEP")
        btn_pasep.grid(row=1, column=4)

        btn_icms = tk.Button(self.window_SN, text="ICMS")
        btn_icms.grid(row=1, column=5)
