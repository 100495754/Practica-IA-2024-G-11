from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class Amount(Trapezoide.Trapezoideloco):
    def __init__(self, amounts):
        self.amounts = amounts
    def amount(self):
        # Calcular los grados de membresía para la edad de 35 años
        Small = self.trapezoidal_membership(self.amounts, -2, -1, 1, 3)
        Medium = self.trapezoidal_membership(self.amounts, 1, 3, 3, 5)
        Big = self.trapezoidal_membership(self.amounts, 3, 5, 5, 7)
        VeryBig = self.trapezoidal_membership(self.amounts, 5, 7, 11, 12)

        return Small, Medium, Big, VeryBig

    def imprimir(self, Big, Medium, Small, VeryBig):
        print("Grado de membresía para 'Small':", Small)
        print("Grado de membresía para 'Medium':", Medium)
        print("Grado de membresía para 'Big':", Big)
        print("Grado de membresía para 'VeryBig':", VeryBig)

    def grafico(self):
        x = np.linspace(0, 8, 1000)

        # Calcular los grados de membresía
        Small = self.trapezoidal_membership(x, -2, -1, 1, 3)
        Medium = self.trapezoidal_membership(x, 1, 3, 3, 5)
        Big = self.trapezoidal_membership(x, 3, 5, 5, 7)
        VeryBig = self.trapezoidal_membership(x, 5, 7, 11, 12)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, Small, label="Small")
        plt.plot(x, Medium, label="Medium")
        plt.plot(x, Big, label="Big")
        plt.plot(x, VeryBig, label="VeryBig")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()