"""Proyecto de IA 23-24"""
import os
from pathlib import Path
from main.metodos_clases.CrearRules import CrearRules
from main.metodos_clases.InputVars import InputVars
from main.variables.Risk import Risk

json_files_path = (str(Path.home()) +
                       "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
def apps_to_dict():
    """Esta función fuzzifica todas las variables por cada application y las guarda en un diccionario de python"""
    input = InputVars()
    input.borrado_y_creado_json()
    input_dict = input.calcular_variables()
    input.guardado_vars(input_dict)
    return input_dict

def rules_to_dict():
    """Esta función clasifica todas las rules en un mismo diccionario de python"""
    rules = CrearRules()
    rules.borrado_y_creado_json()
    rules.crear_json_app()
    a = rules.crear_dictrules()
    rules.guardado_vars(a)
    return a


def calc_risk():
    """Esta funcion recoge ambos diccionarios creados anteriormente y calcula cada riesgo por cada application"""
    applications = apps_to_dict()
    rules = rules_to_dict()
    dic_total = {}
    calculo = CrearRules()
    dic_total = calculo.calcular_riesgos(applications, dic_total, rules)
    return dic_total

def calc_centroide():
    """Esta funcion calcula el centroide por cada application"""
    dict = calc_risk()
    for app in dict:
        low = dict[app]["LowR"]
        med = dict[app]["MediumR"]
        hig = dict[app]["HighR"]
        mi_centroide = Risk(0)
        mi_centroide = mi_centroide.centroide(low, med, hig)

        dict[app]["Centroide"] = mi_centroide
    return dict

def crear_resultado():
    """Esta función recoge en un mismo fichero .txt todos los resultados"""
    file_path = 'resultados.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)  # Elimina el archivo si ya existe

    data = calc_centroide()  # Calcula los centroides y otros datos necesarios
    output_lines = []  # Lista para guardar las líneas de texto

    for key, values in data.items():
        centroide = values.get('Centroide', 'n/a')
        if isinstance(centroide, float):
            centroide = round(centroide, 3)
        # Construye una línea de texto incluyendo el id de la application y el centroide
        line = f"{key}, {centroide}"
        output_lines.append(line)

    # Escribir todas las líneas en el archivo .txt
    with open(file_path, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')



crear_resultado()
validate = input("¿Quieres ver la gráfica resultado de alguna de las aplicaciones? [Y/n]: ")
while not validate.upper() == 'N':
    if validate.upper() == 'Y':
        numero = input("¿Cuál quieres ver?: ")
        numero = str(numero).zfill(4)
        dict = calc_centroide()
        low = dict[str(numero)]["LowR"]
        med = dict[str(numero)]["MediumR"]
        hig = dict[str(numero)]["HighR"]
        centroide = dict[str(numero)]["Centroide"]
        my_risk = Risk(0)
        my_risk.grafico_combinado(low, med, hig, centroide)
    validate = input("¿Quieres ver la gráfica resultado de alguna de las aplicaciones? [Y/n]: ")

