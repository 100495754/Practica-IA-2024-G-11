from scipy.integrate import trapz

from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

class Risk(Trapezoide.Trapezoideloco):
    def __init__(self, risk):
        self.risk = risk
    def risk(self):
        # Calcular los grados de membresía para la edad de 35 años
        LowR = self.trapezoidal_membership(self.risk, -20, -10, 30, 50)
        MediumR= self.trapezoidal_membership(self.risk, 10, 40, 70, 90)
        HighR = self.trapezoidal_membership(self.risk, 50, 70, 100, 111)


        return LowR, MediumR, HighR

    def imprimir(self, adult_x, elder_x, young_x):
        print("Grado de membresía para 'LowR':", young_x)
        print("Grado de membresía para 'adulto':", adult_x)
        print("Grado de membresía para 'HighR':", elder_x)

    def grafico(self):
        x = np.linspace(0, 100, 1000)

        # Calcular los grados de membresía
        LowR = self.trapezoidal_membership(x, -20, -10, 30, 50)
        MediumR = self.trapezoidal_membership(x, 10, 40, 70, 90)
        HighR = self.trapezoidal_membership(x, 50, 70, 100, 111)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, LowR, label="Young")
        plt.plot(x, MediumR, label="Adult")
        plt.plot(x, HighR, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()

    def grafico_combinado(self, low, med, hig, centroide):
        x = np.linspace(0, 100, 1000)

        # Calcular los grados de membresía
        LowR = self.trapezoidal_membership(x, -20, -10, 30, 50)
        MediumR = self.trapezoidal_membership(x, 10, 40, 70, 90)
        HighR = self.trapezoidal_membership(x, 50, 70, 100, 111)

        # Aplicar los grados de activación
        LowR_cutoff = self.cutoff_trapezoidal_membership(LowR, low)
        MediumR_cutoff = self.cutoff_trapezoidal_membership(MediumR, med)
        HighR_cutoff = self.cutoff_trapezoidal_membership(HighR, hig)

        # Combinar las membresías activadas usando el operador máximo
        combined_membership = np.maximum(np.maximum(LowR_cutoff, MediumR_cutoff), HighR_cutoff)

        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(x, combined_membership, 'k', label="Combined Membership")
        # Añadir el punto del centroide
        plt.scatter([centroide], [0], color='red', s=100, zorder=5, label="Centroide")

        # Añadir etiquetas y leyendas
        plt.title("Fuzzy Membership Functions with Centroid")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.ylim(0, 1)
        plt.legend()
        plt.grid(True)
        plt.show()

    def centroide(self, low, medium, high):
        x = np.linspace(0, 100, 10000)
        LowR = self.trapezoidal_membership(x, -20, -10, 30, 50)
        MediumR = self.trapezoidal_membership(x, 10, 40, 70, 90)
        HighR = self.trapezoidal_membership(x, 50, 70, 100, 111)

        # Aplicar los grados de activación
        LowR_cutoff = self.cutoff_trapezoidal_membership(LowR, low)
        MediumR_cutoff = self.cutoff_trapezoidal_membership(MediumR, medium)
        HighR_cutoff = self.cutoff_trapezoidal_membership(HighR, high)

        # Combinar las membresías activadas usando el operador máximo
        combined_membership = np.maximum(np.maximum(LowR_cutoff, MediumR_cutoff), HighR_cutoff)

        # Calcular el centroide
        """Forma1"""
        centroid = fuzz.defuzz(x, combined_membership, 'centroid')
        """Forma2"""
        #numerator = np.trapz(combined_membership * x, x)
        #denominator = np.trapz(combined_membership, x)
        #centroid = numerator / denominator
        return centroid

    # Función para cortar el gráfico trapezoidal hasta un valor específico
    def cutoff_trapezoidal_membership(self, values, threshold):
        """Limitar los valores trapezoidales a un umbral dado."""
        return np.minimum(values, threshold)

risk = Risk(10)
print(risk.centroide(0.5, 0.7, 0.5))
