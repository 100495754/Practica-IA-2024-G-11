from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class IncomeLevel(Trapezoide.Trapezoideloco):
    def __init__(self, age):
        self.edad = age
    def incomelevel(self):
        # Calcular los grados de membresía para la edad de 35 años
        Low = self.trapezoidal_membership(self.edad, -20, -10, 25, 40)
        Med = self.trapezoidal_membership(self.edad, 20, 30, 50, 80)
        Hig = self.trapezoidal_membership(self.edad, 40, 80, 160, 170)

        print("Grado de membresía para 'Low':", Low)
        print("Grado de membresía para 'Med':", Med)
        print("Grado de membresía para 'Hig':", Hig)
        return Low, Med, Hig

    def grafico(self):
        x = np.linspace(0, 150, 1000)

        # Calcular los grados de membresía
        Low = self.trapezoidal_membership(x, -20, -10, 25, 40)
        Med = self.trapezoidal_membership(x, 20, 30, 50, 80)
        Hig = self.trapezoidal_membership(x, 40, 80, 160, 170)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, Low, label="Young")
        plt.plot(x, Med, label="Adult")
        plt.plot(x, Hig, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
