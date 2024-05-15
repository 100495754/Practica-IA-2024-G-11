
from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class Risk(Trapezoide.Trapezoide):
    def __init__(self, risk):
        self.risk = risk
        # Definir el rango universal para la variable Risk
        self.x_risk = np.linspace(0, 100, 1000)
        # Definir los parámetros de las funciones de membresía
        self.lowR_params = [-20, -10, 30, 50]
        self.mediumR_params = [10, 40, 70, 90]
        self.highR_params = [50, 70, 100, 111]
        # Crear las funciones de membresía usando skfuzzy
        self.lowR_mf = fuzz.trapmf(self.x_risk, self.lowR_params)
        self.mediumR_mf = fuzz.trapmf(self.x_risk, self.mediumR_params)
        self.highR_mf = fuzz.trapmf(self.x_risk, self.highR_params)

    def grafico(self):
        x = np.linspace(0, 100, 1000)
        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, self.lowR_mf, label="LowR")
        plt.plot(x, self.mediumR_mf, label="MediumR")
        plt.plot(x, self.highR_mf, label="HighR")
        plt.title("Fuzzy Membership Functions for Risk Categories")
        plt.xlabel("Risk")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()

    def grafico_combinado(self, low, med, high, centroide):
        # Aplicar los grados de activación
        LowR_cutoff = self.cutoff_trapezoidal_membership(self.lowR_mf, low)
        MediumR_cutoff = self.cutoff_trapezoidal_membership(self.mediumR_mf, med)
        HighR_cutoff = self.cutoff_trapezoidal_membership(self.highR_mf, high)

        # Combinar las membresías activadas usando el operador máximo
        combined_membership = np.maximum(np.maximum(LowR_cutoff, MediumR_cutoff), HighR_cutoff)

        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_risk, combined_membership, 'k', label="Combined Membership")
        # Añadir el punto del centroide
        plt.scatter([centroide], [0], color='red', s=100, zorder=5, label="Centroide")

        # Añadir etiquetas y leyendas
        plt.title("Fuzzy Membership Functions with Centroid")
        plt.xlabel("Risk")
        plt.ylabel("Degree of Membership")
        plt.ylim(0, 1)
        plt.legend()
        plt.grid(True)
        plt.show()

    def centroide(self, low, medium, high):
        x = self.x_risk
        # Aplicar los grados de activación
        LowR_cutoff = np.minimum(self.lowR_mf, low)
        MediumR_cutoff = np.minimum(self.mediumR_mf, medium)
        HighR_cutoff = np.minimum(self.highR_mf, high)

        # Combinar las membresías activadas usando el operador máximo
        combined_membership = np.maximum(np.maximum(LowR_cutoff, MediumR_cutoff), HighR_cutoff)
        # Calcular el centroide
        centroid = fuzz.defuzz(x, combined_membership, 'centroid')
        return centroid
