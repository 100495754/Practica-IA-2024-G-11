import json
import os
from pathlib import Path

from main.metodos_clases.json_rules import CrearRules
from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile, readFuzzySetsFile, readRulesFile
from main.variables.Amount import Amount
from main.variables.Assets import Assets
from main.variables.History import History
from main.variables.IncomeLevel import IncomeLevel
from main.variables.Job import Job
from main.metodos_clases.InputVars import InputVars
from main.variables.Risk import Risk

json_files_path = (str(Path.home()) +
                       "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
def apps_to_dict():
    input = InputVars()
    input.borrado_y_creado_json()
    input_dict = input.calcular_variables()
    input.guardado_vars(input_dict)
    return input_dict

def rules_to_dict():
    rules = CrearRules()
    rules.borrado_y_creado_json()
    rules.crear_json_app()
    a = rules.crear_dictrules()
    rules.guardado_vars(a)
    return a


def calc_risk():
        applications = apps_to_dict()
        rules = rules_to_dict()
        dic_total = {}
        calculo = CrearRules()
        dic_total = calculo.calcular_riesgos(applications, dic_total, rules)
        return dic_total

def calc_centroide():
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
    # Datos de entrada
    file_path = 'output.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)  # Elimina el archivo si ya existe

    data = calc_centroide()  # Calcula los centroides y otros datos necesarios
    output_lines = []  # Lista para guardar las líneas de texto

    for key, values in data.items():
        centroide = values.get('Centroide', 'n/a')
        if isinstance(centroide, float):
            centroide = round(centroide, 3)
        # Construye una línea de texto incluyendo los valores de riesgo y el centroide
        line = f"{key}, LowR={values.get('LowR', 0)}, MediumR={values.get('MediumR', 0)}, HighR={values.get('HighR', 0)}, Centroide={centroide}"
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

