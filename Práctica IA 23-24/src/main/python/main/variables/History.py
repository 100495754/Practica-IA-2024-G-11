from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class History(Trapezoide.Trapezoideloco):
    def __init__(self, hist):
        self.hist = hist
    def history(self):
        # Calcular los grados de membresía para la edad de 35 años
        Poor = self.trapezoidal_membership(self.hist, -2, -1, 1, 3)
        Standard = self.trapezoidal_membership(self.hist, 1, 2, 4, 5)
        Good = self.trapezoidal_membership(self.hist, 3, 5, 8, 9)

        print("Grado de membresía para 'Poor':", Poor)
        print("Grado de membresía para 'Standard':", Standard)
        print("Grado de membresía para 'Good':", Good)

        return Poor, Standard,Good

    def grafico(self):
        x = np.linspace(0, 6, 1000)

        # Calcular los grados de membresía
        Poor = self.trapezoidal_membership(x, -2, -1, 1, 3)
        Standard = self.trapezoidal_membership(x, 1, 2, 4, 5)
        Good = self.trapezoidal_membership(x, 3, 5, 8, 9)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, Poor, label="Poor")
        plt.plot(x, Standard, label="Standard")
        plt.plot(x, Good, label="Good")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
