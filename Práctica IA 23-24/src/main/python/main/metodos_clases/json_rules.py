import json
import os
from pathlib import Path
from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile, \
    readFuzzySetsFile, readRulesFile
from main.read_classes.MFIS_Read_Functions import readApplicationsFile
from main.variables.Amount import Amount
from main.variables.Assets import Assets
from main.variables.History import History
from main.variables.IncomeLevel import IncomeLevel
from main.variables.Job import Job


class CrearRules:
    json_files_path = (str(Path.home()) +
                       "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
    file = json_files_path + '/json_rules.json'
    def borrado_y_creado_json(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
        self.crear_json_app()

    def crear_json_app(self):
        try:
            with open(self.file, 'r') as f:
                z = json.load(f)
        except FileNotFoundError:
            z = {}
            with open(self.file, 'w') as f:
                json.dump(z, f)  # Crea un archivo JSON vacío, o ajusta esto según lo que necesites

    def guardado_vars(self, input_dict):
        try:
            with open(self.file, 'w') as f:
                # Guarda el diccionario completo en el archivo JSON, con una indentación de 4 espacios
                json.dump(input_dict, f, indent=4)
        except FileNotFoundError:
            print("File not found")

    def crear_dictrules(self):
        rules = readRulesFile()

        dict_rules = {}

        for rule in rules:
            sub_rule = {}
            if_dict = {}
            for i in rule.antecedent:
                partes = i.split('=')
                if_dict[partes[0]] = partes[1]
            sub_rule["IF"] = if_dict
            partes = rule.consequent.split('=')
            sub_rule[partes[0]] = partes[1]
            dict_rules[rule.ruleName] = sub_rule

        return dict_rules

    def calcular_riesgos(self,applications, dic_total, rules):
        for app in applications:
            aux_dict = {}
            lowR, mediumR, highR = 0, 0, 0
            for rule in rules:
                age, incomelevel, assets, amount, job, history = 0, 0, 0, 0, \
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
                    risk = rules[rule]["Risk"]

                    if risk == "LowR":
                        if lowR < minimo:
                            lowR = minimo
                    elif risk == "MediumR":
                        if mediumR < minimo:
                            mediumR = minimo
                    elif risk == "HighR":
                        if highR < minimo:
                            highR = minimo

            aux_dict["LowR"] = lowR
            aux_dict["MediumR"] = mediumR
            aux_dict["HighR"] = highR
            dic_total[app] = aux_dict
        return dic_total
