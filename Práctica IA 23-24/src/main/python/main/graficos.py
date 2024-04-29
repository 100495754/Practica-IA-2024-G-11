import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Paso 1: Crear las variables del universo
temperature = ctrl.Antecedent(np.arange(10, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Paso 2: Generar funciones de membresía
temperature['low'] = fuzz.trimf(temperature.universe, [10, 10, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 25, 30])
temperature['high'] = fuzz.trimf(temperature.universe, [25, 40, 40])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Paso 3: Crear las reglas
rule1 = ctrl.Rule(temperature['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'], fan_speed['high'])

# Paso 4: Crear y simular el sistema de control
fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan = ctrl.ControlSystemSimulation(fan_control)

# Definir una temperatura específica para probar
fan.input['temperature'] = 30  # Temperatura en grados Celsius

# Calcular la salida
fan.compute()





