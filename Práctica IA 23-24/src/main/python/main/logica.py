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
        for app in applications:
            aux_dict = {}
            for rule in rules:
                age, incomelevel, assets, amount, job, history = 0, 0, 0, 0,\
                                                               0, 0
                salto = False
                aux = []

                if not salto:
                    if "Age" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["Age"]
                        if applications[app]["Age"][valor] > 0:
                            age = applications[app]["Age"][valor]
                            aux.append(age)
                        else:
                            salto = True
                if not salto:
                    if "IncomeLevel" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["IncomeLevel"]
                        if applications[app]["IncomeLevel"][valor] > 0:
                            incomelevel = applications[app]["IncomeLevel"][valor]
                            aux.append(incomelevel)
                        else:
                            salto = True
                if not salto:
                    if "Assets" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["Assets"]
                        if applications[app]["Assets"][valor] > 0:
                            assets = applications[app]["Assets"][valor]
                            aux.append(assets)
                        else:
                            salto = True
                if not salto:
                    if "Amount" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["Amount"]
                        if applications[app]["Amount"][valor] > 0:
                            amount = applications[app]["Amount"][valor]
                            aux.append(amount)
                        else:
                            salto = True
                if not salto:
                    if "Job" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["Job"]
                        if applications[app]["Job"][valor] > 0:
                            job = applications[app]["Job"][valor]
                            aux.append(job)
                        else:
                            salto = True
                if not salto:
                    if "History" in rules[rule]["IF"]:
                        valor = rules[rule]["IF"]["History"]
                        if applications[app]["History"][valor] > 0:
                            history = applications[app]["History"][valor]
                            aux.append(history)
                        else:
                            salto = True
                if not salto:
                    minimo = min(aux)
                    aux_dict[rules[rule]["Risk"]] = minimo
            dic_total[app] = aux_dict
        return dic_total


def prueba():
    # Datos de entrada
    file_path = 'output.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)

    data = calc_risk()
    # Convertir el diccionario a la línea de texto deseada
    for i in data:
        output_lines = []
        for key, values in data.items():
            # Asumimos que LowR podría no estar presente y asignamos un valor por defecto de 0
            line = f"{key}, LowR={values.get('LowR', 0)}, MediumR={values.get('MediumR', 0)}, HighR={values.get('HighR', 0)}"
            output_lines.append(line)

        # Escribir la línea en un archivo .txt
        file_path = 'output.txt'
        with open(file_path, 'w') as file:
            for line in output_lines:
                file.write(line + '\n')

prueba()
#apps_to_dict()
#calc_risk()
