from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class Assets(Trapezoide.Trapezoide):
    def __init__(self, assets):
        self.assets = assets
        # Definir el rango universal
        self.x = np.linspace(0, 50, 1000)
        # Definir los parámetros de las funciones de membresía
        self.Scarce_params = [-2, -1, 5, 20]
        self.Moderate_params = [5, 10, 20, 30]
        self.Abundant_params = [25, 30, 60, 70]
        # Crear las funciones de membresía usando skfuzzy
        self.Scarce_mf = fuzz.trapmf(self.x, self.Scarce_params)
        self.Moderate_mf = fuzz.trapmf(self.x, self.Moderate_params)
        self.Abundant_mf = fuzz.trapmf(self.x, self.Abundant_params)

    def asset(self):
        # Calcular los grados de membresía
        Scarce = fuzz.interp_membership(self.x, self.Scarce_mf, self.assets)
        Moderate = fuzz.interp_membership(self.x, self.Moderate_mf, self.assets)
        Abundant = fuzz.interp_membership(self.x, self.Abundant_mf, self.assets)

        return Scarce, Moderate, Abundant

    def grafico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.Scarce_mf, label="Young")
        plt.plot(self.x, self.Moderate_mf, label="Adult")
        plt.plot(self.x, self.Abundant_mf, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
