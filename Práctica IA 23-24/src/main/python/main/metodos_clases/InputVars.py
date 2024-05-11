
import json
import os
from pathlib import Path
from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile, readFuzzySetsFile
from main.read_classes.MFIS_Read_Functions import readApplicationsFile
from main.variables.Amount import Amount
from main.variables.Assets import Assets
from main.variables.History import History
from main.variables.IncomeLevel import IncomeLevel
from main.variables.Job import Job


class InputVars:
    json_files_path = (str(Path.home()) +
                       "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
    file = json_files_path + '/json_app.json'
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
    def calcular_variables(self):
        """Crea un fichero json con las variables calculadas de cada application y las guarda en un diccionario."""
        app = readApplicationsFile()
        j = 0
        dict = {}
        for i in app:
            temp_dict = {}

            """Edad"""
            data = {}
            edad = app[j].data[0][1]
            algo = Age(edad)
            data["Young"], data["Adult"], data["Elder"] = algo.age()
            temp_dict["Age"] = data

            """IncomeLevel"""
            data = {}
            incomelevel = app[j].data[1][1]
            algo = IncomeLevel(incomelevel)
            data["Low"], data["Med"], data["Hig"] = algo.incomelevel()
            temp_dict["IncomeLevel"] = data

            """Assets"""
            data = {}
            assets = app[j].data[2][1]
            algo = Assets(assets)
            data["Scarce"], data["Moderate"], data["Abundant"] = algo.asset()
            temp_dict["Assets"] = data

            """Amount"""
            data = {}
            amount = app[j].data[3][1]
            algo = Amount(amount)
            data["Small"], data["Medium"], data["Big"], data["VeryBig"] = algo.amount()
            temp_dict["Amount"] = data

            """Job"""
            data = {}
            job = app[j].data[4][1]
            algo = Job(job)
            data["Unstable"], data["Stable"] = algo.job()
            temp_dict["Job"] = data

            """History"""
            data = {}
            history = app[j].data[5][1]
            algo = History(history)
            data["Poor"], data["Standard"], data["Good"] = algo.history()
            temp_dict["History"] = data

            dict[app[j].appId] = temp_dict

            j += 1

        return dict
