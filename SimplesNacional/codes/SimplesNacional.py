import pandas as pd
from tkinter import messagebox

FATURAMENTOMAXIMOSN = 4800000
class SimplesNacional():

    def __init__(self):
        self.faturamento_mensal = []
        self.rb12 = []
        self.imposto = []
        self.porcentagem_aliquota = []
        self.df_client = pd.DataFrame()

    def calcular_faturamento_mensal(self):
        try:
            for valor in self.df_client["Faturamento"]:
                self.faturamento_mensal.append(valor)
        except:
            messagebox.showerror("Erro!", "Erro ao calcular faturamento")
        else:
            messagebox.showinfo("Sucesso", "Faturamento calculado")

    def calcular_rb12(self):
        self.rb12 = []
        i = j = 0
        try:
            for faturamento in self.faturamento_mensal:
                if i <= 11:
                    if i == 0:
                        rb12 = faturamento * 12
                        self.rb12.append(rb12)
                        i += 1
                    else:
                        itens = self.faturamento_mensal[:i + 1]
                        itens = sum(itens)
                        itens = itens / (i + 1)
                        self.rb12.append(itens)
                        i += 1
                else:
                    j = i - 11
                    i += 1
                    itens = self.faturamento_mensal[j:i]
                    itens_somados = sum(itens)
                    self.rb12.append(itens_somados)
        except:
            messagebox.showerror("Erro", "Calcule o faturamento antes de calcular o RB12")
        else:
            messagebox.showinfo("Sucesso", "RB12 Calculado com sucesso")

    def calcular_anexo_I(self): #Comércio
        for valor, faturamento in zip(self.rb12, self.faturamento_mensal):
            if valor <= FATURAMENTOMAXIMOSN:
                if valor <= 180000:
                    porcentagem = 0.04
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 360000:
                    porcentagem = (0.073 * valor - 5940) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 720000:
                    porcentagem = (0.095 * valor - 13860) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 1800000:
                    porcentagem = (0.107 * valor - 22500) / valor
                    imposto = porcentagem * faturamento
                    self.porcentagem_aliquota.append(porcentagem)
                    self.imposto.append(imposto)
                elif valor <= 3600000:
                    porcentagem = (0.143 * valor - 87300) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 4800000:
                    porcentagem = (0.19 * valor - 378000) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
            else:
                print(f"ERRO!\nReceita Bruta maior que 4800000\nRB12 errado: {valor:,.2f}")

    def calcular_anexo_II(self):#Industria
        for valor, faturamento in zip(self.rb12, self.faturamento_mensal):
            if valor <= FATURAMENTOMAXIMOSN:
                if valor <= 180000:
                    porcentagem = 0.045
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 360000:
                    porcentagem = ((valor * 0.078) - 5940) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 720000:
                    porcentagem = ((valor * 0.1) - 13860) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 1800000:
                    porcentagem = ((valor * 0.112) - 22500) / valor
                    imposto = porcentagem * faturamento
                    self.porcentagem_aliquota.append(porcentagem)
                    self.imposto.append(imposto)
                elif valor <= 3600000:
                    porcentagem = ((valor * 0.147) - 87300) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 4800000:
                    porcentagem = ((valor * 0.30) - 378000) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
            else:
                print(f"ERRO!\nFaturamento maior que 4800000\nFaturamento errado: {valor:,.2f}")

    def calcular_anexo_III(self):#Prestadores de serviço
        for valor, faturamento in zip(self.rb12, self.faturamento_mensal):
            if valor <= FATURAMENTOMAXIMOSN:
                if valor <= 180000:
                    porcentagem = 0.06
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 360000:
                    porcentagem = ((valor * 0.112) - 9360) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 720000:
                    porcentagem = ((valor * 0.135) - 17640) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 1800000:
                    porcentagem = ((valor * 0.16) - 35640) / valor
                    imposto = porcentagem * faturamento
                    self.porcentagem_aliquota.append(porcentagem)
                    self.imposto.append(imposto)
                elif valor <= 3600000:
                    porcentagem = ((valor * 0.21) - 125640) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 4800000:
                    porcentagem = ((valor * 0.33) - 648000) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
            else:
                print(f"ERRO!\nFaturamento maior que 4800000\nFaturamento errado: {valor:,.2f}")

    def calcular_anexo_IV(self):#Prestadores de serviço
        for valor, faturamento in zip(self.rb12, self.faturamento_mensal):
            if valor <= FATURAMENTOMAXIMOSN:
                if valor <= 180000:
                    porcentagem = 0.045
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 360000:
                    porcentagem = ((valor * 0.09) - 8100) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 720000:
                    porcentagem = ((valor * 0.102) - 12420) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 1800000:
                    porcentagem = ((valor * 0.14) - 39780) / valor
                    imposto = porcentagem * faturamento
                    self.porcentagem_aliquota.append(porcentagem)
                    self.imposto.append(imposto)
                elif valor <= 3600000:
                    porcentagem = ((valor * 0.22) - 183780) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 4800000:
                    porcentagem = ((valor * 0.33) - 828000) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
            else:
                print(f"ERRO!\nFaturamento maior que 4800000\nFaturamento errado: {valor:,.2f}")

    def calcular_anexo_V(self):#Prestadores de serviço
        for valor, faturamento in zip(self.rb12, self.faturamento_mensal):
            if valor <= FATURAMENTOMAXIMOSN:
                if valor <= 180000:
                    porcentagem = 0.155
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 360000:
                    porcentagem = ((valor * 0.18) - 4500) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = faturamento * porcentagem
                    self.imposto.append(imposto)
                elif valor <= 720000:
                    porcentagem = ((valor * 0.195) - 9900) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 1800000:
                    porcentagem = ((valor * 0.205) - 17100) / valor
                    imposto = porcentagem * faturamento
                    self.porcentagem_aliquota.append(porcentagem)
                    self.imposto.append(imposto)
                elif valor <= 3600000:
                    porcentagem = ((valor * 0.23) - 62100) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
                elif valor <= 4800000:
                    porcentagem = ((valor * 0.305) - 540000) / valor
                    self.porcentagem_aliquota.append(porcentagem)
                    imposto = porcentagem * faturamento
                    self.imposto.append(imposto)
            else:
                print(f"ERRO!\nFaturamento maior que 4800000\nFaturamento errado: {valor:,.2f}")