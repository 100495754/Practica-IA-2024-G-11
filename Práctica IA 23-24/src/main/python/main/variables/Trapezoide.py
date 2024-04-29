
import numpy as np
import matplotlib.pyplot as plt

class Trapezoideloco():
    def trapezoidal_membership(self,x, a, b, c, d):
        """ Calcula el grado de membresía trapezoidal."""
        return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))
