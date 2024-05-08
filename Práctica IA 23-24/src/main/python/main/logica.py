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

def rules_to_dict():
    rules = CrearRules()
    rules.borrado_y_creado_json()
    rules.crear_json_app()
    a = rules.crear_dictrules()
    rules.guardado_vars(a)

def calc_risk():

        json_files_path = (str(Path.home()) +
                           "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
        file = json_files_path + '/json_app.json'
        try:
            with open(file, 'r') as f:
                applications = json.load(f)
        except FileNotFoundError:
            print("File not found. Creating a new file.")
            applications = {}
            with open(file, 'w') as f:
                json.dump(applications, f)
                # Crea un archivo JSON vacío, o ajusta esto según lo que necesites

        file = json_files_path + '/json_rules.json'
        try:
            with open(file, 'r') as f:
                rules = json.load(f)
        except FileNotFoundError:
            print("File not found. Creating a new file.")
            rules = {}
            with open(file, 'w') as f:
                json.dump(rules, f)
                # Crea un archivo JSON vacío, o ajusta esto según lo que necesites

        dic_total = {}
        for app in applications:
            for rule in rules:
                age, incomelevel, assets, amount, job, history = 0, 0, 0, 0,\
                                                               0, 0
                salto = False
                aux = []
                if not salto:
                    if "Age" in rule["IF"]:
                        valor = rule["IF"]["Age"]
                        if app["Age"][valor] > 0:
                            age = app["Age"][valor]
                            aux.append(age)
                        else:
                            salto = True
                if not salto:
                    if "IncomeLevel" in rule["IF"]:
                        valor = rule["IF"]["IncomeLevel"]
                        if app["IncomeLevel"][valor] > 0:
                            incomelevel = app["IncomeLevel"][valor]
                            aux.append(incomelevel)
                        else:
                            salto = True
                if not salto:
                    if "Assets" in rule["IF"]:
                        valor = rule["IF"]["Assets"]
                        if app["Assets"][valor] > 0:
                            assets = app["Assets"][valor]
                            aux.append(assets)
                        else:
                            salto = True
                if not salto:
                    if "Amount" in rule["IF"]:
                        valor = rule["IF"]["Amount"]
                        if app["Amount"][valor] > 0:
                            amount = app["Amount"][valor]
                            aux.append(amount)
                        else:
                            salto = True
                if not salto:
                    if "Job" in rule["IF"]:
                        valor = rule["IF"]["Job"]
                        if app["Job"][valor] > 0:
                            job = app["Job"][valor]
                            aux.append(job)
                        else:
                            salto = True
                if not salto:
                    if "History" in rule["IF"]:
                        valor = rule["IF"]["History"]
                        if app["History"][valor] > 0:
                            history = app["History"][valor]
                            aux.append(history)
                        else:
                            salto = True
                minimo = min(aux)
                dic_total[app][rule][rule["Risk"]] = minimo

        print(dic_total)








#apps_to_dict()
rules_to_dict()
calc_risk()
