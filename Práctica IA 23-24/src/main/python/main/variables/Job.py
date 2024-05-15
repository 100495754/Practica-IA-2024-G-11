
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class Job:
    def __init__(self, job_):
        self.job_ = job_
        # Definir el rango universal
        self.x = np.linspace(0, 5, 1000)
        # Definir los parámetros de las funciones de membresía
        self.Unstable_params = [-2, -1, 1, 2]
        self.Stable_params = [2, 3, 6, 7]
        # Crear las funciones de membresía usando skfuzzy
        self.Unstable_mf = fuzz.trapmf(self.x, self.Unstable_params)
        self.Stable_mf = fuzz.trapmf(self.x, self.Stable_params)

    def job(self):
        # Calcular los grados de membresía
        Unstable = fuzz.interp_membership(self.x, self.Unstable_mf, self.job_)
        Stable = fuzz.interp_membership(self.x, self.Stable_mf, self.job_)
        return Unstable, Stable

    def grafico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.Unstable_mf, label="Small")
        plt.plot(self.x, self.Stable_mf, label="Medium")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
