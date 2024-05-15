
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class IncomeLevel:
    def __init__(self, income):
        self.income = income
        # Definir el rango universal
        self.x = np.linspace(0, 150, 1000)
        # Definir los parámetros de las funciones de membresía
        self.Low_params = [-20, -10, 25, 40]
        self.Med_params = [20, 30, 50, 80]
        self.Hig_params = [40, 80, 160, 170]
        # Crear las funciones de membresía usando skfuzzy
        self.Low_mf = fuzz.trapmf(self.x, self.Low_params)
        self.Med_mf = fuzz.trapmf(self.x, self.Med_params)
        self.Hig_mf = fuzz.trapmf(self.x, self.Hig_params)

    def incomelevel(self):
        # Calcular los grados de membresía
        Low = fuzz.interp_membership(self.x, self.Low_mf, self.income)
        Med = fuzz.interp_membership(self.x, self.Med_mf, self.income)
        Hig = fuzz.interp_membership(self.x, self.Hig_mf, self.income)

        return Low, Med, Hig

    def grafico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.Low_mf, label="Young")
        plt.plot(self.x, self.Med_mf, label="Adult")
        plt.plot(self.x, self.Hig_mf, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
