from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class Amount(Trapezoide.Trapezoide):
    def __init__(self, amounts):
        self.amounts = amounts
        # Definir el rango universal
        self.x = np.linspace(0, 8, 1000)
        # Definir los parámetros de las funciones de membresía
        self.Small_params = [-2, -1, 1, 3]
        self.Medium_params = [1, 3, 3, 5]
        self.Big_params = [3, 5, 5, 7]
        self.VeryBig_params = [5, 7, 11, 12]
        # Crear las funciones de membresía usando skfuzzy
        self.Small_mf = fuzz.trapmf(self.x, self.Small_params)
        self.Medium_mf = fuzz.trapmf(self.x, self.Medium_params)
        self.Big_mf = fuzz.trapmf(self.x, self.Big_params)
        self.VeryBig_mf = fuzz.trapmf(self.x, self.VeryBig_params)

    def amount(self):
        # Calcular los grados de membresía
        Small = fuzz.interp_membership(self.x, self.Small_mf, self.amounts)
        Medium = fuzz.interp_membership(self.x, self.Medium_mf, self.amounts)
        Big = fuzz.interp_membership(self.x, self.Big_mf, self.amounts)
        VeryBig = fuzz.interp_membership(self.x, self.VeryBig_mf, self.amounts)

        return Small, Medium, Big, VeryBig

    def grafico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.Small_mf, label="Small")
        plt.plot(self.x, self.Medium_mf, label="Medium")
        plt.plot(self.x, self.Big_mf, label="Big")
        plt.plot(self.x, self.VeryBig_mf, label="VeryBig")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
