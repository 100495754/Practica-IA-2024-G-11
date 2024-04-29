import numpy as np

import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_membership(x, a, b, c, d):
    """ Calcula el grado de membresía trapezoidal."""
    return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))

# Definir el rango de edades
x = np.linspace(0, 100, 1000)

# Calcular los grados de membresía
young = trapezoidal_membership(x, 20, 30, 40, 50)
adult = trapezoidal_membership(x, 30, 50, 65, 75)
elder = trapezoidal_membership(x, 65, 85, 150, 175)

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
