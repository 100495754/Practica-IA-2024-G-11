from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class History(Trapezoide.Trapezoide):
    def __init__(self, hist):
        self.hist = hist
        # Definir el rango universal
        self.x = np.linspace(0, 6, 1000)
        # Definir los parámetros de las funciones de membresía
        self.Poor_params = [-2, -1, 1, 3]
        self.Standard_params = [1, 2, 4, 5]
        self.Good_params = [3, 5, 8, 9]
        # Crear las funciones de membresía usando skfuzzy
        self.Poor_mf = fuzz.trapmf(self.x, self.Poor_params)
        self.Standard_mf = fuzz.trapmf(self.x, self.Standard_params)
        self.Good_mf = fuzz.trapmf(self.x, self.Good_params)

    def history(self):
        # Calcular los grados de membresía
        Poor = fuzz.interp_membership(self.x, self.Poor_mf, self.hist)
        Standard = fuzz.interp_membership(self.x, self.Standard_mf, self.hist)
        Good = fuzz.interp_membership(self.x, self.Good_mf, self.hist)

        return Poor, Standard, Good

    def grafico(self):
        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.Poor_mf, label="Poor")
        plt.plot(self.x, self.Standard_mf, label="Standard")
        plt.plot(self.x, self.Good_mf, label="Good")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
