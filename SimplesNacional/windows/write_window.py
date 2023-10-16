import tkinter as tk
from SimplesNacional.windows.select_window import WindowSelect
from tkinter import ttk
from SimplesNacional.codes.SimplesNacional import SimplesNacional
from tkinter import messagebox
from tkinter import filedialog
import Constantes

class Window_write:
    def __init__(self):
        self.window_write = tk.Tk()
        self.window_write.title("Digitar Faturamento")
        self.butons()
        self.messages()
        self.combo_box()
        self.style()
        self.simples_nacional = SimplesNacional()
        self.window_write.mainloop()

    def style(self):
        self.window_write.configure(bg=Constantes.bck_color)

    def back_select_window(self):
        self.window_write.destroy()
        self.window_select = WindowSelect()

    def _exportar_arquivo(self):
        if not self.simples_nacional.porcentagem_aliquota:
            messagebox.showerror("Erro", "Calcular as alíquotas antes de exportar o arquivo!")
            return

        arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivo do Excel", "*.xlsx")])
        if arquivo:
            if not arquivo.endswith(".xlsx"):
                arquivo += ".xlsx"

            self.simples_nacional.df_client["Faturamento"] = self.simples_nacional.faturamento_mensal
            self.simples_nacional.df_client["RB12"] = self.simples_nacional.rb12
            self.simples_nacional.df_client["Porcentagem"] = self.simples_nacional.porcentagem_aliquota
            self.simples_nacional.df_client["Aliquota"] = self.simples_nacional.imposto

            try:
                self.simples_nacional.df_client.to_excel(arquivo, index=False)
                messagebox.showinfo("Êxito", "Arquivo exportado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao exportar o arquivo:\n{str(e)}")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado para exportar!")

    def _selecionar_anexo(self):
        anexo_selecionado = self.escolha_anexo.get()
        try:
            if anexo_selecionado == "Anexo I":
                self.simples_nacional.calcular_anexo_I()
            elif anexo_selecionado == "Anexo II":
                self.simples_nacional.calcular_anexo_II()
            elif anexo_selecionado == "Anexo III":
                self.simples_nacional.calcular_anexo_III()
            elif anexo_selecionado == "Anexo IV":
                self.simples_nacional.calcular_anexo_IV()
            elif anexo_selecionado == "Anexo V":
                self.simples_nacional.calcular_anexo_V()
        except:
            messagebox.showerror("Erro", "Calcule tudo antes de selecionar o anexo")
        else:
            messagebox.showinfo("Sucesso", f"As aliquotas foram calculadas com base no {anexo_selecionado}")

    def _calcular_faturamento(self):
        faturamentos = self.texto_faturamento.get("1.0", tk.END).strip().split("\n")
        if faturamentos:
            for valor in faturamentos:
                valor = float(valor)
                self.simples_nacional.faturamento_mensal.append(valor)
            messagebox.showinfo("Sucesso", "Faturamento calculado com sucesso")
        else:
            messagebox.showerror("ERRO!", "Digite os faturamentos na caixa de texto")

    def butons(self):
        bnt_calcular = tk.Button(self.window_write,text="Calcular", command=self.mix_rb,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        bnt_calcular.grid(row=2,column=1)

        btn_back = tk.Button(self.window_write, text="<-", command=self.back_select_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_back.grid(row=0, column=0, sticky="NW")

        btn_exportar = tk.Button(self.window_write, text="Exportar arquivo", command=self._exportar_arquivo,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_exportar.grid(row=3, column=1, sticky="s")

    def messages(self):
        mensagem = tk.Label(self.window_write,
                            text="Digite no espaço abaixo os faturamentos mensais\ndigite um faturamento por linha",font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        mensagem.grid(row=1, column=0)

        self.texto_faturamento = tk.Text(self.window_write, height=10, width=30,font=Constantes.btn_font, bg=Constantes.btn_color, fg=Constantes.btn_txt_color)
        self.texto_faturamento.grid(row=2, column=0, padx=10, pady=5)


    def combo_box(self):
        self.escolha_anexo = ttk.Combobox(self.window_write,values=["Anexo I", "Anexo II", "Anexo III", "Anexo IV", "Anexo V"])
        self.escolha_anexo.grid(row=1, column=1, sticky="S")

    def mix_rb(self):
        self._calcular_faturamento()
        self.simples_nacional.calcular_rb12()
        self._selecionar_anexo()

