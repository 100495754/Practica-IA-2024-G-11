
import skfuzzy as fuzz
import numpy as np

class Trapezoide():
    def trapezoidal_membership(self, x, a, b, c, d):
        return fuzz.trapmf(x, [a, b, c, d])
    # Función para cortar el gráfico trapezoidal hasta un valor específico
    def cutoff_trapezoidal_membership(self, values, threshold):
        """Limitar los valores trapezoidales a un umbral dado."""
        return np.minimum(values, threshold)
