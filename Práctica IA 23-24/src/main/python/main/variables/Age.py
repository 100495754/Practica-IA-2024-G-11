from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class Age(Trapezoide.Trapezoideloco):
    def __init__(self, age):
        self.edad = age
    def age(self):
        # Calcular los grados de membresía para la edad de 35 años
        young_x = self.trapezoidal_membership(self.edad, -20, -10, 30, 40)
        adult_x = self.trapezoidal_membership(self.edad, 20, 30, 50, 65)
        elder_x = self.trapezoidal_membership(self.edad, 50, 65, 150, 175)


        return young_x, adult_x, elder_x

    def imprimir(self, adult_x, elder_x, young_x):
        print("Grado de membresía para 'joven':", young_x)
        print("Grado de membresía para 'adulto':", adult_x)
        print("Grado de membresía para 'anciano':", elder_x)

    def grafico(self):
        x = np.linspace(0, 100, 1000)

        # Calcular los grados de membresía
        young = self.trapezoidal_membership(x, -20, -10, 30, 40)
        adult = self.trapezoidal_membership(x, 20, 30, 50, 65)
        elder = self.trapezoidal_membership(x, 50, 65, 150, 175)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, young, label="Young")
        plt.plot(x, adult, label="Adult")
        plt.plot(x, elder, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
