from main.variables import Trapezoide
import numpy as np
import matplotlib.pyplot as plt


class Job(Trapezoide.Trapezoideloco):
    def __init__(self, job_):
        self.job_ = job_
    def job(self):
        # Calcular los grados de membresía para la edad de 35 años
        Unstable = self.trapezoidal_membership(self.job_, -2, -1, 1, 2)
        Stable = self.trapezoidal_membership(self.job_, 2, 3, 6, 7)

        print("Grado de membresía para 'Unstable':", Unstable)
        print("Grado de membresía para 'Stable':", Stable)

        return Unstable, Stable

    def grafico(self):
        x = np.linspace(0, 5, 1000)

        # Calcular los grados de membresía
        Unstable = self.trapezoidal_membership(x, -2, -1, 1, 2)
        Stable = self.trapezoidal_membership(x, 2, 3, 6, 7)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(x, Unstable, label="Small")
        plt.plot(x, Stable, label="Medium")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
