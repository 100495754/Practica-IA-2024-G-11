from main.variables import Trapezoide
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class Age(Trapezoide.Trapezoide):
    def __init__(self, age):
        self.edad = age
        # Definir el rango universal para la variable Age
        self.x_age = np.linspace(0, 100, 1000)
        # Definir los parámetros de las funciones de membresía
        self.young_params = [-20, -10, 30, 40]
        self.adult_params = [20, 30, 50, 65]
        self.elder_params = [50, 65, 150, 175]
        # Crear las funciones de membresía usando skfuzzy
        self.young_mf = fuzz.trapmf(self.x_age, self.young_params)
        self.adult_mf = fuzz.trapmf(self.x_age, self.adult_params)
        self.elder_mf = fuzz.trapmf(self.x_age, self.elder_params)

    def age(self):
        # Calcular los grados de membresía para la edad específica
        young_x = fuzz.interp_membership(self.x_age, self.young_mf, self.edad)
        adult_x = fuzz.interp_membership(self.x_age, self.adult_mf, self.edad)
        elder_x = fuzz.interp_membership(self.x_age, self.elder_mf, self.edad)

        return young_x, adult_x, elder_x

    def grafico(self):
        """Muestra el grafico para esta variable"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_age, self.young_mf, label="Young")
        plt.plot(self.x_age, self.adult_mf, label="Adult")
        plt.plot(self.x_age, self.elder_mf, label="Elder")
        plt.title("Fuzzy Membership Functions for Age Categories")
        plt.xlabel("Age")
        plt.ylabel("Degree of Membership")
        plt.legend()
        plt.grid(True)
        plt.show()
