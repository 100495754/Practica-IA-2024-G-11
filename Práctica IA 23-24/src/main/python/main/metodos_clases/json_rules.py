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
            print("File not found. Creating a new file.")
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
