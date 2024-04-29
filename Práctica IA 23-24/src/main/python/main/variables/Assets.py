from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class Assets(Trapezoide.Trapezoideloco):
    def __init__(self, assets):
        self.assets = assets
    def asset(self):
        # Calcular los grados de membresía para la edad de 35 años
        Scarce = self.trapezoidal_membership(self.assets, -2, -1, 5, 20)
        Moderate = self.trapezoidal_membership(self.assets, 5, 10, 20, 30)
        Abundant = self.trapezoidal_membership(self.assets, 25, 30, 60, 70)

        print("Grado de membresía para 'Scarce':", Scarce)
        print("Grado de membresía para 'Moderate':", Moderate)
        print("Grado de membresía para 'Abundant':", Abundant)

    def grafico(self):
        x = np.linspace(0, 50, 1000)

        # Calcular los grados de membresía
        Scarce = self.trapezoidal_membership(x, -2, -1, 5, 20)
        Moderate = self.trapezoidal_membership(x, 5, 10, 20, 30)
        Abundant = self.trapezoidal_membership(x, 25, 30, 60, 70)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, Scarce, label="Young")
        plt.plot(x, Moderate, label="Adult")
        plt.plot(x, Abundant, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
