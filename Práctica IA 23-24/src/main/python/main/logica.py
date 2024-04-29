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

app = readApplicationsFile()
j = 0
json_files_path = (str(Path.home()) +
                                   "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
file = json_files_path + '/json_app.json'
if os.path.isfile(file):
    os.remove(file)
try:
    with open(file, 'r') as f:
        z = json.load(f)
except FileNotFoundError:
    print("File not found. Creating a new file.")
    z = {}
    with open(file, 'w') as f:
        json.dump(z, f)  # Crea un archivo JSON vacío, o ajusta esto según lo que necesites

dict = {}
for i in app:
    """Edad"""
    data = {}
    temp_dict = {}
    edad = app[j].data[0][1]
    print(edad)
    algo = Age(edad)
    data["Young"],data["Adult"],data["Elder"] = algo.age()
    temp_dict["Age"] = data
    print(data)
    algo.age()

    """IncomeLevel"""
    data = {}
    incomelevel = app[j].data[1][1]
    print(incomelevel)
    algo = IncomeLevel(incomelevel)
    data["Low"], data["Med"], data["Hig"] = algo.incomelevel()
    temp_dict["IncomeLevel"] = data
    algo.incomelevel()

    """Assets"""
    data = {}
    assets = app[j].data[2][1]
    print(assets)
    algo = Assets(assets)
    data["Scarce"], data["Moderate"], data["Abundant"] = algo.asset()
    temp_dict["Assets"] = data
    algo.asset()

    """Amount"""
    data = {}
    amount = app[j].data[3][1]
    print(amount)
    algo = Amount(amount)
    data["Small"], data["Medium"], data["Big"], data["VeryBig"]= algo.amount()
    temp_dict["Amount"] = data
    algo.amount()

    """Job"""
    data = {}
    job = app[j].data[4][1]
    print(job)
    algo = Job(job)
    data["Unstable"], data["Stable"] = algo.job()
    temp_dict["Job"] = data
    algo.job()

    """History"""
    data = {}
    history = app[j].data[5][1]
    print(history)
    algo = History(history)
    data["Poor"], data["Standard"], data["Good"] = algo.history()
    temp_dict["History"] = data
    algo.history()

    dict[app[j].appId] = temp_dict
    print(dict)


    j += 1
    print("")
    print("")


try:
    with open(file, 'w') as f:
        # Guarda el diccionario completo en el archivo JSON, con una indentación de 4 espacios
        json.dump(dict, f, indent=4)
except FileNotFoundError:
    print("File not found")

