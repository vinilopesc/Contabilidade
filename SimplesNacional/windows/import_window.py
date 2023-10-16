import tkinter as tk
from SimplesNacional.windows.select_window import WindowSelect
from tkinter import ttk
from SimplesNacional.codes.SimplesNacional import SimplesNacional
from tkinter import filedialog
from tkinter import messagebox
import os
import pandas as pd
import Constantes


class Window_import:
    def __init__(self):
        self.window_import = tk.Tk()
        self.window_import.title("Importar arquivo")
        self.butons()
        self.messages()
        self.image_combo_box()
        self.style()
        self.simples_nacional = SimplesNacional()
        self.window_import.mainloop()


    def style(self):
        self.window_import.configure(bg=Constantes.bck_color)

    def back_select_window(self):
        self.window_import.destroy()
        self.window_select = WindowSelect()
    def butons(self):
        btn_back = tk.Button(self.window_import, text="<-", command=self.back_select_window,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_back.grid(row=0, column=0, sticky="NW")

        botao_importar = tk.Button(self.window_import, text="Importar arquivo", command=self._mix_math,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        botao_importar.grid(row=1, column=1)

        btn_selecionar_anexo = tk.Button(self.window_import, text="Selecionar Anexo", command=self._selecionar_anexo,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_selecionar_anexo.grid(row=2, column=2)

        btn_exportar = tk.Button(self.window_import, text="Exportar resultado", command=self._exportar_arquivo,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        btn_exportar.grid(row=3, column=1, sticky="N")

    def messages(self):
        mensagem_imposto = tk.Label(self.window_import, text="Selecione o arquivo => ",font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        mensagem_imposto.grid(row=1, column=0, sticky='w')

        mensagem_imagem = tk.Label(self.window_import,
                                   text="A planilha deve ter uma coluna\n com o nome 'Faturamento'\nComo na imagem abaixo:",font=Constantes.txt_font, bg=Constantes.bck_color, fg=Constantes.fr_color)
        mensagem_imagem.grid(row=2, column=0, sticky='w')

    def image_combo_box(self):
        self.imagem = tk.PhotoImage(file="Image_xlsx.PNG")
        label_imagem = tk.Label(self.window_import, image=self.imagem,background=Constantes.btn_color,foreground=Constantes.btn_txt_color,font=Constantes.btn_font)
        label_imagem.grid(row=3, column=0, sticky='w')

        self.escolha_anexo = ttk.Combobox(self.window_import, values=["Anexo I", "Anexo II", "Anexo III", "Anexo IV", "Anexo V"])
        self.escolha_anexo.grid(row=2, column=1)

    def _importar_arquivo(self):
        arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Arquivo do Excel", "*.xlsx")])
        if arquivo:
            if not os.path.exists(arquivo):
                messagebox.showerror("Erro", "Arquivo não encontrado!")
            self.simples_nacional.df_client = pd.read_excel(arquivo)
            messagebox.showinfo("Êxito", "Arquivo importado e processado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado!")

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

    def _mix_math(self):
        self._importar_arquivo()
        self.simples_nacional.calcular_faturamento_mensal()
        self.simples_nacional.calcular_rb12()
